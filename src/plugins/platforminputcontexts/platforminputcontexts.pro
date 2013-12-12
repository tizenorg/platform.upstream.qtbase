TEMPLATE = subdirs

#!contains(DEFINES,Q_OS_LINUX_TIZEN_MOBILE):!contains(DEFINES,Q_OS_LINUX_TIZEN_SIMULATOR): {
    qtHaveModule(dbus) {
        !mac:!win32:SUBDIRS += ibus
    }

    unix:!macx:!contains(DEFINES, QT_NO_XKBCOMMON): {
        SUBDIRS += compose
    }
#} else {
#    SUBDIRS += tizenscim
#}
