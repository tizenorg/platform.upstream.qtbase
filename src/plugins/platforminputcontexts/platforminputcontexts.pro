TEMPLATE = subdirs

qtHaveModule(dbus) {
!mac:!win32:SUBDIRS += ibus
}

contains(QT_CONFIG, xcb-plugin): SUBDIRS += compose

contains(DEFINES,TIZEN_SCIM): SUBDIRS += tizenscim
