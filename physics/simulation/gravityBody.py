from collisions.Rectangle2D import *



class GravityBody(Rectangle2D.Rectangle2D):

    GRAVITY = 9.8 # (m/s)

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.velocityY = 0
        self.wheight = 80
        
    
    def update(self, deltaTime):
        self.velocityY += GravityBody.GRAVITY * deltaTime / self.wheight

    def draw(self, surface):
        self.drawDebug(surface)
    
    def __str__(self) -> str:
        return f"GravityObject x={self.x}, y={self.y}, w={self.w}, h={self.h}, velocityY={self.velocityY}, weight={self.weight}"


"""""

class Character:

    def __init__(self):
        self.collider = GravityBody(...)
        self.animationManager = AnimationManager(...)

"""


"""
Animation -> des images qui tournent en boucle
AnimationManager -> choisir quelle Animation jouer {"run":Animation0, "jump":Amination1...}

"""


""""
Animation
-> fn getCurrentImage() -> Image

""""



""""
public class AnimationManager {
	
	public String current;
	private Animation current_animation;
	private Map<String, Animation> animation_map = new HashMap<>(); // {name : animation}
	
	public AnimationManager() {
		
	}
	
	public Image getCurrentImage() {
		if(current_animation != null) {
			return current_animation.get_current_frame();
		}
		return null;
	}
	
	public Animation getCurrentAnim() {
		return this.current_animation;
	}
	
	public void update() {
		if(this.current_animation != null) {
			this.current_animation.update();
		}
	}
	
	public void add(String key, Animation anim) {
		this.animation_map.put(key, anim);
	}
	
	public void remove(String key) {
		this.animation_map.remove(key);
	}
	
	public Animation get(String key) {
		return this.animation_map.get(key);
	}
	
	public void setToCurrent(String key) {
		current_animation = animation_map.get(key);
		current = key;
	}
	
	public void play() {
		current_animation.replay();
	}
	
	public void play(String key) {
		setToCurrent(key);
		play();
	}
	
	public void pause() {
		current_animation.pause();
	}
	
	public void pause(String key) {
		setToCurrent(key);	
		pause();
	}
	
	public void resume() {
		current_animation.resume();
	}
	
	public void resume(String key) {
		setToCurrent(key);
		current_animation.resume();
	}
}


"""