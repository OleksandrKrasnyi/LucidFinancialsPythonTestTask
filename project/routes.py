from fastapi import APIRouter, Depends, HTTPException, status
from functools import lru_cache
from datetime import datetime, timedelta
import jwt
from dependencies import get_db, get_current_user
from schemas import UserCreate, UserLogin, PostCreate, PostResponse
from models import User, Post
from config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRY

router = APIRouter()

def create_token(email: str) -> str:
    """Create JWT token with expiration time"""
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRY)
    to_encode = {"sub": email, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/signup")
async def signup(user: UserCreate, db=Depends(get_db)):
    """Register new user"""
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(email=user.email, password=user.password)  # Hash password in production
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    token = create_token(user.email)
    return {"token": token}

@router.post("/login")
async def login(user: UserLogin, db=Depends(get_db)):
    """Authenticate user"""
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or db_user.password != user.password:  # Check hash in production
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token(user.email)
    return {"token": token}

@router.post("/posts", response_model=PostResponse)
async def add_post(post: PostCreate, current_user=Depends(get_current_user), db=Depends(get_db)):
    """Add new post"""
    db_post = Post(text=post.text, user_id=current_user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/posts", response_model=list[PostResponse])
@lru_cache(maxsize=128)
async def get_posts(current_user=Depends(get_current_user), db=Depends(get_db)):
    """Get all user posts with caching"""
    posts = db.query(Post).filter(Post.user_id == current_user.id).all()
    return posts

@router.delete("/posts/{post_id}")
async def delete_post(post_id: int, current_user=Depends(get_current_user), db=Depends(get_db)):
    """Delete post"""
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == current_user.id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}