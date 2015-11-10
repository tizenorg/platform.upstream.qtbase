TARGET = qeglfs

PLUGIN_TYPE = platforms
PLUGIN_CLASS_NAME = QEglFSIntegrationPlugin
!equals(TARGET, $$QT_DEFAULT_QPA_PLUGIN): PLUGIN_EXTENDS = -
load(qt_plugin)

# Avoid X11 header collision
DEFINES += MESA_EGL_NO_X11_HEADERS

QT += platformsupport-private eglfs_device_lib-private

SOURCES += $$PWD/qeglfsmain.cpp

OTHER_FILES += $$PWD/eglfs.json
