from OpenGL.GL import GL_TRUE
import glfw
from OpenGL.GL import *


class Application:

    def __init__(self):
        self.window = None

    def startup(self) -> None:
        raise Exception('Bootstrap must be defined. '
                        'This method is run once before '
                        'entering the rendering process.')

    def shutdown(self) -> None:
        raise Exception('Shutdown must be defined.'
                        'This method is run once before '
                        'exiting the whole application.')

    def before_render(self) -> None:
        pass

    def render(self) -> None:
        raise Exception('Render must be defined. '
                        'Otherwise, it does not render anything.')

    def after_render(self) -> None:
        pass

        # Initialize glfw

    def run(self) -> None:
        if not glfw.init():
            print('Cannot initialize GLFW. Check its installation.')
            return

        # Configure window's context
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        # Create a new window
        self.window = glfw.create_window(800, 600, 'Chapter this', None, None)

        if not self.window:
            print('Cannot open new window')
            glfw.terminate()
            return

        glfw.make_context_current(self.window)

        self.startup()

        while not glfw.window_should_close(self.window):
            self.before_render()
            self.render()
            self.after_render()

        self.shutdown()

        glfw.terminate()
