# The MIT License (MIT)
# 
# Copyright (c) 2013 Tomasz Olszak <olszak.tomasz@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This file is based on qtbase.spec from Mer project
# http://merproject.org

# libQtPlatformSupport is not built as a shared library, only as a
# static .a lib-archive. By default the OBS build removes all discovered
# libFOO.a files and as such rpmlint never complains about
# installed-but-unpackaged static libs.
# This flag tells rpmbuild to behave.

%if "%{tizen}" == "2.1"
%define qt_tizen_2 1
%define profile mobile
%define _with_x 1
%else
%define qt_tizen_2 0
%endif

%bcond_with wayland
%bcond_with x


# Version is the date of latest commit in qtbase, followed by 'g' + few
# characters of the last git commit ID.
# NOTE: tarball's prefix is 'qt5-base' until version number starts to
# make sense. This allows to update spec contents easily as snapshots
# evolve.
Name:       qt5
Summary:    Cross-platform application and UI framework
Version:    5.2.90+alpha
Release:    0
Group:      Base/Libraries
License:    LGPL-2.1+ or GPL-3.0
URL:        http://qt.digia.com
Source0:    %{name}-%{version}.tar.bz2
Source1:    macros.qt5-default
Source100:  qtbase-rpmlintrc
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libjpeg-devel
BuildRequires:  pam-devel
BuildRequires:  readline-devel
BuildRequires:  python
BuildRequires:  pkgconfig(fontconfig)
%if !%{qt_tizen_2}
BuildRequires:  pkgconfig(xkbcommon)
%endif
%if "%{profile}" != "mobile"
BuildRequires:  pkgconfig(egl)
%else
BuildRequires:  pkgconfig(scim)
%endif
BuildRequires:  pkgconfig(gles20)
%if %{with x}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(aul)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
%endif


%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

%package tools
Summary:    Development tools for qtbase
Group:      Base/Libraries
Requires:   qtchooser

%description tools
This package contains useful tools for Qt development

%package qtcore
Summary:    The QtCore library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtcore
This package contains the QtCore library

%package qtcore-devel
Summary:    Development files for QtCore
Group:      Base/Libraries
Requires:   %{name}-qmake
Requires:   %{name}-tools
Requires:   %{name}-qtcore = %{version}-%{release}
Requires:   fontconfig-devel
Requires:   qtchooser

%description qtcore-devel
This package contains the files necessary to develop applications
that use the QtCore


%package qmake
Summary:    QMake
Group:      Base/Libraries
Requires:   qtchooser

%description qmake
This package contains qmake


%package plugin-bearer-connman
Summary:    Connman bearer plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-connman
This package contains the connman bearer plugin


%package plugin-bearer-generic
Summary:    Connman generic plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-generic
This package contains the connman generic bearer plugin


%package plugin-bearer-nm
Summary:    Connman generic plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-nm
This package contains the connman NetworkManager bearer plugin


%package plugin-imageformat-gif
Summary:    Gif image format plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-gif
This package contains the gif imageformat plugin


%package plugin-imageformat-ico
Summary:    Ico image format plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-ico
This package contains the ico imageformat plugin


%package plugin-imageformat-jpeg
Summary:    JPEG image format plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-jpeg
This package contains the JPEG imageformat plugin

%package plugin-platform-minimal
Summary:    Minimal platform plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-minimal
This package contains the minimal platform plugin

%package plugin-platform-offscreen
Summary:    Offscreen platform plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-offscreen
This package contains the offscreen platform plugin

%package plugin-platform-eglfs
Summary:    Eglfs platform plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-eglfs
This package contains the eglfs platform plugin

%package plugin-platform-minimalegl
Summary:    Minimalegl platform plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-minimalegl
This package contains the minimalegl platform plugin

%package plugin-platform-linuxfb
Summary:    Linux framebuffer platform plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-linuxfb
This package contains the linuxfb platform plugin for Qt

%if %{with x}

%package plugin-platform-xcb
Summary:    XCB platform plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-xcb
This package contains the XCB platform plugin

%endif

%package plugin-printsupport-cups
Summary:    CUPS print support plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-printsupport-cups
This package contains the CUPS print support plugin

%package plugin-accessible-widgets
Summary:     Accessible widgets plugin
Group:       Base/Libraries
Requires:    %{name}-qtcore = %{version}-%{release}

%description plugin-accessible-widgets
This package contains the access widgets plugin

%package plugin-sqldriver-sqlite
Summary:    Sqlite sql driver plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-sqldriver-sqlite
This package contains the sqlite sql driver plugin

%if !%{qt_tizen_2}
%package plugin-platforminputcontext-ibus
Summary:    The ibus platform import context plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platforminputcontext-ibus
This package contains the ibus platform input context plugin

%package plugin-platforminputcontext-compose
Summary:    Compose input context platform plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platforminputcontext-compose
This package contains compose platform inputcontext plugin
%endif

%if "%profile" == "mobile"
%package plugin-platform-inputcontext-tizenscim
Summary:    tizenscim input context platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-inputcontext-tizenscim
This package contains tizenscim platform inputcontext plugin
%endif

%package plugin-generic-evdev
Summary:    The evdev generic plugin
Group:      Base/Libraries
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-generic-evdev
This package contains evdev plugins

%package qtdbus
Summary:    The QtDBus library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtdbus
This package contains the QtDBus library


%package qtdbus-devel
Summary:    Development files for QtDBus
Group:      Base/Libraries
Requires:   %{name}-qtdbus = %{version}-%{release}
Requires:   pkgconfig(dbus-1)

%description qtdbus-devel
This package contains the files necessary to develop
applications that use QtDBus


%package qtgui
Summary:    The QtGui Library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtgui
This package contains the QtGui library


%package qtgui-devel
Summary:    Development files for QtGui
Group:      Base/Libraries
Requires:   %{name}-qtgui = %{version}-%{release}
Requires:   %{name}-qtopengl-devel

%description qtgui-devel
This package contains the files necessary to develop
applications that use QtGui


%package qtnetwork
Summary:    The QtNetwork library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtnetwork
This package contains the QtNetwork library


%package qtnetwork-devel
Summary:    Development files for QtNetwork
Group:      Base/Libraries
Requires:   %{name}-qtnetwork = %{version}-%{release}

%description qtnetwork-devel
This package contains the files necessary to develop
applications that use QtNetwork

%package qtopengl
Summary:    The QtOpenGL library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtopengl
This package contains the QtOpenGL library


%package qtopengl-devel
Summary:    Development files for QtOpenGL
Group:      Base/Libraries
Requires:   %{name}-qtopengl = %{version}-%{release}
Requires:   pkgconfig(gles20)
%if "%{profile}" != "mobile"
Requires:   pkgconfig(egl)
%endif


%description qtopengl-devel
This package contains the files necessary to develop
applications that use QtOpenGL


%package qtsql
Summary:    The QtSql library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtsql
This package contains the QtSql library

%package qtsql-devel
Summary:    Development files for QtSql
Group:      Base/Libraries
Requires:   %{name}-qtsql = %{version}-%{release}

%description qtsql-devel
This package contains the files necessary to develop
applications that use QtSql


%package qttest
Summary:    The QtTest library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qttest
This package contains the QtTest library


%package qttest-devel
Summary:    Development files for QtTest
Group:      Base/Libraries
Requires:   %{name}-qttest = %{version}-%{release}

%description qttest-devel
This package contains the files necessary to develop
applications that use QtTest


%package qtxml
Summary:    The QtXml library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtxml
This package contains the QtXml library

%package qtxml-devel
Summary:    Development files for QtXml
Group:      Base/Libraries
Requires:   %{name}-qtxml = %{version}-%{release}

%description qtxml-devel
This package contains the files necessary to develop
applications that use QtXml


%package qtwidgets
Summary:    The QtWidgets library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtwidgets
This package contains the QtWidgets library

%package qtwidgets-devel
Summary:    Development files for QtWidgets
Group:      Base/Libraries
Requires:   %{name}-qtwidgets = %{version}-%{release}

%description qtwidgets-devel
This package contains the files necessary to develop
applications that use QtWidgets

%package qtplatformsupport-devel
Summary:    Development files for QtPlatformSupport
Group:      Base/Libraries

%description qtplatformsupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport

%package qtbootstrap-devel
Summary:    Development files for QtBootstrap
Group:      Base/Libraries

%description qtbootstrap-devel
This package contains the files necessary to develop
applications that use QtBootstrap

%package qtprintsupport
Summary:    The QtPrintSupport
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtprintsupport
This package contains the QtPrintSupport library

%package qtprintsupport-devel
Summary:    Development files for QtPrintSupport
Group:      Base/Libraries
Requires:   %{name}-qtprintsupport = %{version}-%{release}

%description qtprintsupport-devel
This package contains the files necessary to develop
applications that use QtPrintSupport

%package qtconcurrent
Summary:    QtConcurrent library
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtconcurrent
This package contains the QtConcurrent library

%package qtconcurrent-devel
Summary:    Development files for QtConcurrent
Group:      Base/Libraries
Requires:   %{name}-qtconcurrent = %{version}-%{release}

%description qtconcurrent-devel
This package contains the files necessary to develop
applications that use QtConcurrent

%package -n qt5-default
Summary:    Qt5 development defaults packafge
Group:      Development/Libraries
Requires:   qtchooser
Provides:   qt-default
Conflicts:   qt4-default

%description -n qt5-default
Qt is a cross-platform application and UI framework. Using Qt, you can write
web-enabled applications once and deploy them across desktop, mobile and
embedded operating systems without rewriting the source code.

This package contains the Qt5 development defaults package



##### Build section

%prep
%setup -q -n qt5-%{version}/qtbase

%build
touch .git

MAKEFLAGS=%{?_smp_mflags} \
./configure --disable-static \
    -confirm-license \
%if ! 0%{?qt5_release_build}
    -developer-build \
    -no-warnings-are-errors \
%endif
    -platform devices/linux-g++-tizen \
%if "%{profile}" != ""
    -device-option TIZEN_PROFILE=%{profile} \
%endif
%if %{with wayland}
    -device-option QT_QPA_DEFAULT_PLATFORM=wayland \
%else
%if %{with x}
    -device-option QT_QPA_DEFAULT_PLATFORM=xcb \
%endif
%endif
    -opengl es2 \
    -prefix "%{_prefix}" \
    -bindir "%{_libdir}/qt5/bin" \
    -libdir "%{_libdir}" \
    -docdir "%{_docdir}/qt5/" \
    -headerdir "%{_includedir}/qt5" \
    -datadir "%{_datadir}/qt5" \
    -plugindir "%{_libdir}/qt5/plugins" \
    -importdir "%{_libdir}/qt5/imports" \
    -translationdir "%{_datadir}/qt5/translations" \
    -sysconfdir "%{_sysconfdir}/xdg" \
    -examplesdir "%{_libdir}/qt5/examples" \
    -archdatadir "%{_datadir}/qt5" \
    -testsdir "%{_libdir}/qt5/tests" \
    -qmldir "%{_libdir}/qt5/qml" \
    -libexecdir "%{_libdir}/qt5/libexec" \
    -opensource \
    -no-sql-ibase \
    -no-sql-mysql \
    -no-sql-odbc \
    -no-sql-psql \
    -plugin-sql-sqlite \
    -no-sql-sqlite2 \
    -no-sql-tds \
    -system-sqlite \
    -audio-backend \
    -system-zlib \
    -system-libpng \
    -system-libjpeg \
    -no-rpath \
    -optimized-qmake \
    -dbus-linked \
%if ! 0%{?qt5_release_build}
    -no-strip \
    -no-separate-debug-info \
%endif
    -verbose \
    -no-gtkstyle \
    -no-openvg \
    -nomake tests \
    -nomake examples \
    -no-xinput2 \
%if %{with x}
    -xcb \
    -qt-xcb
%else 
    -no-xcb
%endif


make %{?_smp_mflags}


%install
rm -rf %{buildroot}
INSTALL_ROOT=%{buildroot} %{__make} install

find %{buildroot}%{_docdir}/qt5/ -type f -exec chmod ugo-x {} \;

# Make sure these are around
mkdir -p %{buildroot}%{_includedir}/qt5/
mkdir -p %{buildroot}%{_datadir}/qt5/
mkdir -p %{buildroot}%{_libdir}/qt5/plugins/
mkdir -p %{buildroot}%{_libdir}/qt5/imports/
mkdir -p %{buildroot}%{_libdir}/qt5/translations/
mkdir -p %{buildroot}%{_libdir}/qt5/examples/
#
# Install qmake rpm macros
install -D -p -m 0644 %{_sourcedir}/macros.qt5-default \
%{buildroot}%{_sysconfdir}/rpm/macros.qt5-default

# Add a configuration link for qtchooser - the 5.conf is installed by qtchooser
mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser
ln -s %{_sysconfdir}/xdg/qtchooser/5.conf %{buildroot}%{_sysconfdir}/xdg/qtchooser/default.conf

#
%fdupes %{buildroot}%{_libdir}
%fdupes %{buildroot}%{_includedir}
%fdupes %{buildroot}%{_datadir}


#### Pre/Post section

%post qtcore
/sbin/ldconfig
%postun qtcore
/sbin/ldconfig

%post qtdbus
/sbin/ldconfig
%postun qtdbus
/sbin/ldconfig

%post qtsql
/sbin/ldconfig
%postun qtsql
/sbin/ldconfig

%post qtnetwork
/sbin/ldconfig
%postun qtnetwork
/sbin/ldconfig

%post qtgui
/sbin/ldconfig
%postun qtgui
/sbin/ldconfig

%post qttest
/sbin/ldconfig
%postun qttest
/sbin/ldconfig

%post qtopengl
/sbin/ldconfig
%postun qtopengl
/sbin/ldconfig

%post qtxml
/sbin/ldconfig
%postun qtxml
/sbin/ldconfig

%post qtprintsupport
/sbin/ldconfig
%postun qtprintsupport
/sbin/ldconfig

%post qtwidgets
/sbin/ldconfig
%postun qtwidgets
/sbin/ldconfig

%post qtconcurrent 
/sbin/ldconfig
%postun qtconcurrent 
/sbin/ldconfig

#### File section

# There is no naked qt5 package

%files tools
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/moc
%{_libdir}/qt5/bin/rcc
%{_libdir}/qt5/bin/syncqt.pl
%{_libdir}/qt5/bin/uic
%{_libdir}/qt5/bin/qdoc
%{_libdir}/qt5/bin/qlalr
%{_docdir}/qt5/*

%files qtcore
%defattr(-,root,root,-)
%dir %{_includedir}/qt5/
%dir %{_datadir}/qt5/
%dir %{_libdir}/qt5/plugins/
%dir %{_libdir}/qt5/imports/
%dir %{_libdir}/qt5/translations/
%dir %{_libdir}/qt5/examples/
%{_libdir}/libQt5Core.so.*

%files qtcore-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtCore
%{_libdir}/libQt5Core.prl
%{_libdir}/libQt5Core.la
%{_libdir}/libQt5Core.so
%{_libdir}/pkgconfig/Qt5Core.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_core.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_core_private.pri
%{_libdir}/cmake

%files qmake
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/qmake
%{_datadir}/qt5/mkspecs/aix-*
%{_datadir}/qt5/mkspecs/blackberry*
%{_datadir}/qt5/mkspecs/common
%{_datadir}/qt5/mkspecs/cygwin-*
%{_datadir}/qt5/mkspecs/darwin-*
%{_datadir}/qt5/mkspecs/features
%{_datadir}/qt5/mkspecs/freebsd-*
%{_datadir}/qt5/mkspecs/hpux-*
%{_datadir}/qt5/mkspecs/hpuxi-*
%{_datadir}/qt5/mkspecs/hurd-g++
%{_datadir}/qt5/mkspecs/irix-*
%{_datadir}/qt5/mkspecs/linux-*
%{_datadir}/qt5/mkspecs/lynxos-*
%{_datadir}/qt5/mkspecs/macx-*
%{_datadir}/qt5/mkspecs/netbsd-*
%{_datadir}/qt5/mkspecs/openbsd-*
%{_datadir}/qt5/mkspecs/qconfig.pri
%{_datadir}/qt5/mkspecs/qfeatures.pri
%{_datadir}/qt5/mkspecs/qmodule.pri
%{_datadir}/qt5/mkspecs/qnx*
%{_datadir}/qt5/mkspecs/sco-*
%{_datadir}/qt5/mkspecs/solaris-*
%{_datadir}/qt5/mkspecs/tru64-*
%{_datadir}/qt5/mkspecs/unixware-*
%{_datadir}/qt5/mkspecs/unsupported
%{_datadir}/qt5/mkspecs/win32-g++
%{_datadir}/qt5/mkspecs/win32-icc
%{_datadir}/qt5/mkspecs/win32-msvc20*
%{_datadir}/qt5/mkspecs/wince*
%{_datadir}/qt5/mkspecs/devices
%{_datadir}/qt5/mkspecs/qdevice.pri
%{_datadir}/qt5/mkspecs/winphone-arm-msvc2012
%{_datadir}/qt5/mkspecs/winphone-x86-msvc2012
%{_datadir}/qt5/mkspecs/winrt-arm-msvc2012
%{_datadir}/qt5/mkspecs/winrt-x64-msvc2012
%{_datadir}/qt5/mkspecs/winrt-x86-msvc2012
%{_datadir}/qt5/mkspecs/winrt-arm-msvc2013
%{_datadir}/qt5/mkspecs/winrt-x64-msvc2013
%{_datadir}/qt5/mkspecs/winrt-x86-msvc2013
%config(noreplace) %{_sysconfdir}/rpm/macros.qt5-default

%files qtdbus
%defattr(-,root,root,-)
%{_libdir}/libQt5DBus.so.*


%files qtdbus-devel
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/qdbuscpp2xml
%{_libdir}/qt5/bin/qdbusxml2cpp
%{_includedir}/qt5/QtDBus
%{_libdir}/libQt5DBus.so
%{_libdir}/libQt5DBus.prl
%{_libdir}/libQt5DBus.la
%{_libdir}/pkgconfig/Qt5DBus.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_dbus.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_dbus_private.pri


%files qtgui
%defattr(-,root,root,-)
%{_libdir}/libQt5Gui.so.*


%files qtgui-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtGui
%{_libdir}/libQt5Gui.prl
%{_libdir}/libQt5Gui.la
%{_libdir}/libQt5Gui.so
%{_libdir}/pkgconfig/Qt5Gui.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_gui.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_gui_private.pri


%files qtnetwork
%defattr(-,root,root,-)
%{_libdir}/libQt5Network.so.*


%files qtnetwork-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtNetwork
%{_libdir}/libQt5Network.prl
%{_libdir}/libQt5Network.la
%{_libdir}/libQt5Network.so
%{_libdir}/pkgconfig/Qt5Network.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_network.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_network_private.pri


%files qtopengl
%defattr(-,root,root,-)
%{_libdir}/libQt5OpenGL.so.*


%files qtopengl-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtOpenGL
%{_includedir}/qt5/QtOpenGLExtensions
%{_libdir}/libQt5OpenGL.prl
%{_libdir}/libQt5OpenGL.la
%{_libdir}/libQt5OpenGLExtensions.prl
%{_libdir}/libQt5OpenGLExtensions.la
%{_libdir}/libQt5OpenGL.so
%{_libdir}/libQt5OpenGLExtensions.a
%{_libdir}/pkgconfig/Qt5OpenGL.pc
%{_libdir}/pkgconfig/Qt5OpenGLExtensions.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_opengl.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_opengl_private.pri
%{_datadir}/qt5/mkspecs/android-g++/qmake.conf
%{_datadir}/qt5/mkspecs/android-g++/qplatformdefs.h
%{_datadir}/qt5/mkspecs/modules/qt_lib_openglextensions.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_openglextensions_private.pri


%files qtsql
%defattr(-,root,root,-)
%{_libdir}/libQt5Sql.so.*


%files qtsql-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtSql
%{_libdir}/libQt5Sql.prl
%{_libdir}/libQt5Sql.la
%{_libdir}/libQt5Sql.so
%{_libdir}/pkgconfig/Qt5Sql.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_sql.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_sql_private.pri


%files qttest
%defattr(-,root,root,-)
%{_libdir}/libQt5Test.so.*

%files qttest-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtTest
%{_libdir}/libQt5Test.prl
%{_libdir}/libQt5Test.la
%{_libdir}/libQt5Test.so
%{_libdir}/pkgconfig/Qt5Test.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_testlib.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_testlib_private.pri

%files qtxml
%defattr(-,root,root,-)
%{_libdir}/libQt5Xml.so.*

%files qtxml-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtXml
%{_libdir}/libQt5Xml.prl
%{_libdir}/libQt5Xml.la
%{_libdir}/libQt5Xml.so
%{_libdir}/pkgconfig/Qt5Xml.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_xml.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_xml_private.pri

%files qtwidgets
%defattr(-,root,root,-)
%{_libdir}/libQt5Widgets.so.*

%files qtwidgets-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtWidgets
%{_libdir}/libQt5Widgets.prl
%{_libdir}/libQt5Widgets.la
%{_libdir}/libQt5Widgets.so
%{_libdir}/pkgconfig/Qt5Widgets.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_widgets.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_widgets_private.pri

%files qtplatformsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtPlatformSupport
%{_libdir}/libQt5PlatformSupport.prl
%{_libdir}/libQt5PlatformSupport.la
%{_libdir}/libQt5PlatformSupport.a
%{_libdir}/pkgconfig/Qt5PlatformSupport.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_platformsupport_private.pri

%files qtbootstrap-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Bootstrap.prl
%{_libdir}/libQt5Bootstrap.la
%{_libdir}/libQt5Bootstrap.a
%{_libdir}/pkgconfig/Qt5Bootstrap.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_bootstrap_private.pri

%files qtprintsupport
%defattr(-,root,root,-)
%{_libdir}/libQt5PrintSupport.so.*

%files qtprintsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtPrintSupport
%{_libdir}/libQt5PrintSupport.prl
%{_libdir}/libQt5PrintSupport.la
%{_libdir}/libQt5PrintSupport.so
%{_libdir}/pkgconfig/Qt5PrintSupport.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_printsupport.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_printsupport_private.pri

%files qtconcurrent
%defattr(-,root,root,-)
%{_libdir}/libQt5Concurrent.so.*

%files qtconcurrent-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtConcurrent
%{_libdir}/libQt5Concurrent.prl
%{_libdir}/libQt5Concurrent.la
%{_libdir}/libQt5Concurrent.so
%{_libdir}/pkgconfig/Qt5Concurrent.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_concurrent.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_concurrent_private.pri

# Plugin packages

%files plugin-bearer-connman
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqconnmanbearer.so

%files plugin-bearer-generic
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqgenericbearer.so

%files plugin-bearer-nm
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqnmbearer.so

%files plugin-imageformat-gif
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqgif.so

%files plugin-imageformat-ico
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqico.so

%files plugin-imageformat-jpeg
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqjpeg.so

%files plugin-platform-minimal
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqminimal.so

%files plugin-platform-offscreen
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqoffscreen.so

%files plugin-platform-eglfs
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqeglfs.so

%files plugin-platform-minimalegl
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqminimalegl.so

%files plugin-platform-linuxfb
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqlinuxfb.so

%if %{with x}

%files plugin-platform-xcb
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqxcb.so

%endif

%files plugin-printsupport-cups
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/printsupport/libcupsprintersupport.so

%files plugin-accessible-widgets
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/accessible/libqtaccessiblewidgets.so

%files plugin-sqldriver-sqlite
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sqldrivers/libqsqlite.so

%if !%{qt_tizen_2}
%files plugin-platforminputcontext-ibus
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so

%files plugin-platforminputcontext-compose
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/libcomposeplatforminputcontextplugin.so
%endif

%if "%{profile}" == "mobile"
%files plugin-platform-inputcontext-tizenscim
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/libtizenscimplatforminputcontextplugin.so
%endif

%files plugin-generic-evdev
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/generic/libqevdev*plugin.so

%files -n qt5-default
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/qtchooser/default.conf

#### No changelog section, separate $pkg.changes contains the history
