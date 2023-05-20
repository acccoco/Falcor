add_plugin(wireframe)

target_sources(wireframe PRIVATE
    wireframe.cpp
    wireframe.h
    wireframe.3d.slang
)

target_copy_shaders(wireframe RenderPasses/wireframe)

target_source_group(wireframe "RenderPasses")
