from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
from application import Application


class App(Application):

    def __init__(self):
        super(App, self).__init__()
        self.program = None
        self.vertex_array_object = None

    @staticmethod
    def shaders_bunch() -> GLuint:
        # Load shaders' sources
        handle = open('./chap2/vertex_shader.glsl', 'r')
        vertex_shader_source = handle.read()
        handle = open('./chap2/fragment_shader.glsl', 'r')
        fragment_shader_source = handle.read()

        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, vertex_shader_source)
        glCompileShader(vertex_shader)

        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, fragment_shader_source)
        glCompileShader(fragment_shader)

        program = glCreateProgram()
        glAttachShader(program, vertex_shader)
        glAttachShader(program, fragment_shader)
        glLinkProgram(program)

        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

        return program

    def startup(self):
        self.program = self.shaders_bunch()
        self.vertex_array_object = glGenVertexArrays(1)
        glBindVertexArray(self.vertex_array_object)

    def shutdown(self):
        glDeleteVertexArrays(1, [self.vertex_array_object])
        glDeleteProgram(self.program)

    def before_render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program)

    def render(self):
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glfw.poll_events()
        glfw.swap_buffers(self.window)
