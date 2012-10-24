%define		major_version		3.6
# Minimum GNOME Shell version supported
%define		global min_gs_version	%{major_version}.0

Summary:	Modify and extend GNOME Shell functionality and behavior
Name:		gnome-shell-extensions
Version:	%{major_version}.0
Release:	1
Group:		X11/Applications
# The entire source code is GPLv2+ except lib/convenience.js which is BSD
License:	GPLv2+ and BSD
URL:		http://live.gnome.org/GnomeShell/Extensions
# Using git archive since upstream doesn't publish tarballs on ftp.gnome.org
# anymore
# $ git clone git://git.gnome.org/gnome-shell-extensions/
# $ cd gnome-shell-extensions/
# $ git archive --format=tar --prefix=%{name}-%{version}/ %{version} | xz > ../%{name}-%{version}.tar.xz
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	849a020b25595b173ce99bac452f7db2
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	gnome-desktop-devel
BuildRequires:	libgtop-devel
Requires:	gnome-shell >= %{min_gs_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Shell Extensions is a collection of extensions providing
additional and optional functionality to GNOME Shell.

Enabled extensions:
  - alternate-tab
  - alternative-status-menu
  - apps-menu
  - auto-move-windows
  - dock
  - drive-menu
  - native-window-placement
  - places-menu
  - systemMonitor
  - user-theme
  - windowsNavigator
  - workspace-indicator
  - xrandr-indicator
  - gajim

%package common
Summary:	Files common to GNOME Shell Extensions
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell >= %{min_gs_version}

%description -n gnome-shell-extensions-common
GNOME Shell Extensions is a collection of extensions providing
additional and optional functionality to GNOME Shell. Common files and
directories needed by extensions are provided here.

%package -n gnome-shell-extension-alternate-tab
Summary:	Classic Alt+Tab behavior. Window based instead of app based
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description -n gnome-shell-extension-alternate-tab
Lets you use classic Alt+Tab (window-based instead of app-based) in
GNOME Shell. GNOME Shell groups multiple instances of the same
application together. This extension disables grouping.

%package -n gnome-shell-extension-alternative-status-menu
Summary:	For those who want a power off item visible at all the time
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description -n gnome-shell-extension-alternative-status-menu
For those who want a power off item visible at all the time, replaces
GNOME Shell status menu with one featuring separate Suspend and Power
Off. Adds the ability to hibernate as well.

%package -n gnome-shell-extension-apps-menu
Summary:	Application menu for GNOME Shell
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description  -n gnome-shell-extension-apps-menu
Add a GNOME 2.x style menu for applications.

%package -n gnome-shell-extension-auto-move-windows
Summary:	Assign specific workspaces to applications
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description -n gnome-shell-extension-auto-move-windows
Lets you manage your workspaces more easily, assigning a specific
workspace to each application as soon as it creates a window, in a
manner configurable with a GSettings key.

%package -n gnome-shell-extension-dock
Summary:	Shows a dock-style task switcher permanently
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description -n gnome-shell-extension-dock
Shows a dock-style task switcher on the right side of the screen
permanently.

%package -n gnome-shell-extension-drive-menu
Summary:	Disk device manager in the system status area
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description -n gnome-shell-extension-drive-menu
Adds a menu in the system status area that tracks removable disk
devices attached and offers to browse them and eject/unmount them.

%package -n gnome-shell-extension-gajim
Summary:	Gajim IM integration
License:	GPL v2+
Group:		X11/Applications
Requires:	gajim
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description  -n gnome-shell-extension-gajim
Display Gajim incoming chats as notifications in the Shell message
tray.

%package -n gnome-shell-extension-native-window-placement
Summary:	Arrange windows in overview in a more native way
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description  -n gnome-shell-extension-native-window-placement
This extension employs an algorithm (taken from KDE) for layouting the
thumbnails in the overview that more closely reflects the positions
and relative sizes of the actual windows, instead of using a fixed
grid.

%package -n gnome-shell-extension-places-menu
Summary:	Places menu indicator in the system status area
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description -n gnome-shell-extension-places-menu
Adds a menu in the system status area that resembles the Places menu
from GNOME 2.x

%package -n gnome-shell-extension-systemMonitor
Summary:	Monitor your system status
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}
Requires:	libgtop

%description -n gnome-shell-extension-systemMonitor
Monitor your system status

%package -n gnome-shell-extension-user-theme
Summary:	Lets the user select a custom theme for the shell
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description -n gnome-shell-extension-user-theme
Lets the user select a custom theme for the Gnome shell. It will allow
you to apply a style from
/.themes/[themeName]/gnome-shell/gnome-shell.css

%package -n gnome-shell-extension-windowsNavigator
Summary:	Keyboard selection of windows and work-spaces in overlay mode
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description -n gnome-shell-extension-windowsNavigator
Allow keyboard selection of windows and work-spaces in overlay mode in
GNOME Shell. Switch to overview mode (press the windows or alt+f1 key)
and press the alt key to show numbers over windows. Press any number
to switch to the corresponding window.

%package -n gnome-shell-extension-workspace-indicator
Summary:	Workspace Indicator
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description -n gnome-shell-extension-workspace-indicator
Put an indicator on the panel signaling in which workspace you are,
and give you the possibility of switching to another one.

%package -n gnome-shell-extension-xrandr-indicator
Summary:	Monitor status indicator
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell-extensions-common = %{version}-%{release}

%description  -n gnome-shell-extension-xrandr-indicator
This extension adds a systems status menu for rotating monitors
(overrides what is currently provided by gnome-settings-daemon.

%prep
%setup -q
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%build
%configure \
	 \
	--enable-extensions="alternate-tab \
	alternative-status-menu \
	apps-menu \
	auto-move-windows \
	dock \
	drive-menu \
	native-window-placement \
	places-menu \
	systemMonitor \
	user-theme \
	windowsNavigator \
	workspace-indicator \
	xrandr-indicator
	gajim" \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n gnome-shell-extension-alternate-tab
%glib_compile_schemas

%postun -n gnome-shell-extension-alternate-tab
%glib_compile_schemas

%post -n gnome-shell-extension-alternative-status-menu
%glib_compile_schemas

%postun -n gnome-shell-extension-alternative-status-menu
%glib_compile_schemas

%post -n gnome-shell-extension-auto-move-windows
%glib_compile_schemas

%postun -n gnome-shell-extension-auto-move-windows
%glib_compile_schemas

%post -n gnome-shell-extension-dock
%glib_compile_schemas

%postun -n gnome-shell-extension-dock
%glib_compile_schemas

%post -n gnome-shell-extension-native-window-placement
%glib_compile_schemas

%postun -n gnome-shell-extension-native-window-placement
%glib_compile_schemas

%post -n gnome-shell-extension-user-theme
%glib_compile_schemas

%postun -n gnome-shell-extension-user-theme
%glib_compile_schemas

%files common -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING NEWS README
%dir %{_datadir}/gnome-shell/extensions

%files -n gnome-shell-extension-alternate-tab
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.alternate-tab.gschema.xml
%{_datadir}/gnome-shell/extensions/alternate-tab*

%files -n gnome-shell-extension-alternative-status-menu
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.alternative-status-menu.gschema.xml
%{_datadir}/gnome-shell/extensions/alternative-status-menu*

%files -n gnome-shell-extension-apps-menu
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/apps-menu*

%files -n gnome-shell-extension-auto-move-windows
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
%{_datadir}/gnome-shell/extensions/auto-move-windows*

%files -n gnome-shell-extension-dock
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.dock.gschema.xml
%{_datadir}/gnome-shell/extensions/dock*

%files -n gnome-shell-extension-drive-menu
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/drive-menu*

%files -n gnome-shell-extension-gajim
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/gajim*

%files -n gnome-shell-extension-native-window-placement
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/gnome-shell/extensions/native-window-placement*

%files -n gnome-shell-extension-places-menu
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/places-menu*

%files -n gnome-shell-extension-systemMonitor
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/systemMonitor*

%files -n gnome-shell-extension-user-theme
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
%{_datadir}/gnome-shell/extensions/user-theme*

%files -n gnome-shell-extension-windowsNavigator
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/windowsNavigator*

%files -n gnome-shell-extension-workspace-indicator
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/workspace-indicator*

%files -n gnome-shell-extension-xrandr-indicator
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/xrandr-indicator*
