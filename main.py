import sys
sys.path = sorted(sys.path, key=lambda x: 'site-packages' in x)

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import parentController, enfantController, adminController, tempsEcranController, videoController, saisonController, serieController, categorieController, categorieVideoController 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
appli = FastAPI()
origins = [
    "http://localhost:3000",  
    "http://localhost:8000",  
   
]

appli.add_middleware(
    CORSMiddleware,
     allow_origins=["*"],  # Permettre ces origines
    allow_credentials=True,
    allow_methods=["*"],  # Permettre toutes les méthodes HTTP
    allow_headers=["*"],  # Permettre tous les en-têtes
)


appli.include_router(enfantController.router, prefix="/enfant", tags=["enfant"])
appli.include_router(parentController.router, prefix="/parent", tags=["parent"])
appli.include_router(adminController.router, prefix="/admin", tags=["admin"])
appli.include_router(tempsEcranController.router, prefix="/tempsEcran", tags=["tempsEcran"])
appli.include_router(videoController.router, prefix="/video", tags=["video"])
appli.include_router(saisonController.router, prefix="/saison", tags=["saison"])
appli.include_router(serieController.router, prefix="/serie", tags=["serie"])
appli.include_router(categorieController.router, prefix="/categorie", tags=["categorie"])
appli.include_router(categorieVideoController.router, prefix="/categorie_video", tags=["categorie_video"])
# app.include_router(auth.router, prefix="/categorie", tags=["categorie"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


appli.mount("/videos", StaticFiles(directory="media/videos"), name="videos")

appli.mount("/images", StaticFiles(directory="media/couvertures"), name="images")


# @app.get("/media")
# async def read_video():
#     """
#     ## Get Video
#     This endpoint serves the video file `videoBanner2.mp4`.

#     - **Path:** `/media/videos/videoBanner2.mp4`
#     """
#     return RedirectResponse(url="media/videos/videoBanner2.mp4")

