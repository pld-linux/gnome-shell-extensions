%define		major_version		3.14
# Minimum GNOME Shell version supported
%define		global min_gs_version	%{major_version}.0

Summary:	Modify and extend GNOME Shell functionality and behavior
Name:		gnome-shell-extensions
Version:	%{major_version}.0
Release:	1
Group:		X11/Applications
# The entire source code is GPLv2+ except lib/convenience.js which is BSD
License:	GPLv2+ and BSD
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell-extensions/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	9ba3cb7f22185365108c69074577a975
URL:		http://live.gnome.org/GnomeShell/Extensions
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel
BuildRequires:	intltool
BuildRequires:	libgtop-devel >= 2.28.3
BuildRequires:	pkgconfig >= 1:0.22
Requires:	gnome-shell >= %{min_gs_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ext_prefix	gnome-shell-extension

%description
GNOME Shell Extensions is a collection of extensions providing
additional and optional functionality to GNOME Shell.

Enabled extensions:
  - alternate-tab
  - apps-menu
  - auto-move-windows
  - drive-menu
  - launch-new-instance
  - native-window-placement
  - places-menu
  - screenshot-window-sizer
  - systemMonitor
  - user-theme
  - window-list
  - windowsNavigator
  - workspace-indicator

%package common
Summary:	Files common to GNOME Shell Extensions
License:	GPL v2+
Group:		X11/Applications
Requires:	gnome-shell >= %{min_gs_version}
Obsoletes:	gnome-shell-extension-alternative-status-menu < 3.10.1
Obsoletes:	gnome-shell-extension-default-min-max < 3.8.3.1
Obsoletes:	gnome-shell-extension-dock < 3.8.0
Obsoletes:	gnome-shell-extension-gajim < 3.8.0
Obsoletes:	gnome-shell-extension-static-workspaces < 3.8.3.1
Obsoletes:	gnome-shell-extension-xrandr-indicator < 3.10.1

%description common
GNOME Shell Extensions is a collection of extensions providing
additional and optional functionality to GNOME Shell. Common files and
directories needed by extensions are provided here.

%package -n gnome-classic-session
Summary:	GNOME "classic" mode session
License:	GPL v2+
Group:		X11/Applications
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{ext_prefix}-alternate-tab = %{version}-%{release}
Requires:	%{ext_prefix}-apps-menu = %{version}-%{release}
Requires:	%{ext_prefix}-launch-new-instance = %{version}-%{release}
Requires:	%{ext_prefix}-places-menu = %{version}-%{release}
Requires:	%{ext_prefix}-window-list = %{version}-%{release}
Requires:	gnome-session >= 1:3.14.0

%description -n gnome-classic-session
This package contains the required components for the GNOME Shell
"classic" mode, which aims to provide a GNOME 2-like user interface.

%package -n %{ext_prefix}-alternate-tab
Summary:	Classic Alt+Tab behavior. Window based instead of app based
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-alternate-tab
Lets you use classic Alt+Tab (window-based instead of app-based) in
GNOME Shell. GNOME Shell groups multiple instances of the same
application together. This extension disables grouping.

%package -n %{ext_prefix}-apps-menu
Summary:	Application menu for GNOME Shell
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description  -n %{ext_prefix}-apps-menu
Add a GNOME 2.x style menu for applications.

%package -n %{ext_prefix}-auto-move-windows
Summary:	Assign specific workspaces to applications
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-auto-move-windows
Lets you manage your workspaces more easily, assigning a specific
workspace to each application as soon as it creates a window, in a
manner configurable with a GSettings key.

%package -n %{ext_prefix}-drive-menu
Summary:	Disk device manager in the system status area
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-drive-menu
Adds a menu in the system status area that tracks removable disk
devices attached and offers to browse them and eject/unmount them.

%package -n %{ext_prefix}-launch-new-instance
Summary:	Always launch a new application instance for GNOME Shell
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description  -n %{ext_prefix}-launch-new-instance
This GNOME Shell extension modifies the behavior of clicking in the
dash and app launcher to always launch a new application instance.

%package -n %{ext_prefix}-native-window-placement
Summary:	Arrange windows in overview in a more native way
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-native-window-placement
This extension employs an algorithm (taken from KDE) for layouting the
thumbnails in the overview that more closely reflects the positions
and relative sizes of the actual windows, instead of using a fixed
grid.

%package -n %{ext_prefix}-places-menu
Summary:	Places menu indicator in the system status area
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-places-menu
Adds a menu in the system status area that resembles the Places menu
from GNOME 2.x

%package -n %{ext_prefix}-screenshot-window-sizer
Summary:	Screenshot window sizer for GNOME Shell
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-screenshot-window-sizer
This GNOME Shell extension allows to easily resize windows for GNOME
Software screenshots.

%package -n %{ext_prefix}-systemMonitor
Summary:	Monitor your system status
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	libgtop

%description -n %{ext_prefix}-systemMonitor
Monitor your system status

%package -n %{ext_prefix}-user-theme
Summary:	Lets the user select a custom theme for the shell
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-user-theme
Lets the user select a custom theme for the Gnome shell. It will allow
you to apply a style from
/.themes/[themeName]/gnome-shell/gnome-shell.css

%package -n %{ext_prefix}-window-list
Summary:	Display a window list at the bottom of the screen in GNOME Shell
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-window-list
This GNOME Shell extension displays a window list at the bottom of the
screen.

%package -n %{ext_prefix}-windowsNavigator
Summary:	Keyboard selection of windows and work-spaces in overlay mode
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-windowsNavigator
Allow keyboard selection of windows and work-spaces in overlay mode in
GNOME Shell. Switch to overview mode (press the windows or alt+f1 key)
and press the alt key to show numbers over windows. Press any number
to switch to the corresponding window.

%package -n %{ext_prefix}-workspace-indicator
Summary:	Workspace Indicator
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-workspace-indicator
Put an indicator on the panel signaling in which workspace you are,
and give you the possibility of switching to another one.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-extensions="all"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Drop useless example extension
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/example*
%{__rm} $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.example.gschema.xml

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n gnome-classic-session
%glib_compile_schemas

%postun -n gnome-classic-session
%glib_compile_schemas

%post -n %{ext_prefix}-auto-move-windows
%glib_compile_schemas

%postun -n %{ext_prefix}-auto-move-windows
%glib_compile_schemas

%post -n %{ext_prefix}-native-window-placement
%glib_compile_schemas

%postun -n %{ext_prefix}-native-window-placement
%glib_compile_schemas

%post -n %{ext_prefix}-screenshot-window-sizer
%glib_compile_schemas

%postun -n %{ext_prefix}-screenshot-window-sizer
%glib_compile_schemas

%post -n %{ext_prefix}-user-theme
%glib_compile_schemas

%postun -n %{ext_prefix}-user-theme
%glib_compile_schemas

%post -n %{ext_prefix}-window-list
%glib_compile_schemas

%postun -n %{ext_prefix}-window-list
%glib_compile_schemas

%files common -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING NEWS README
%dir %{_datadir}/gnome-shell/extensions

%files -n gnome-classic-session
%defattr(644,root,root,755)
%{_desktopdir}/gnome-shell-classic.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.classic-overrides.gschema.xml
%{_datadir}/gnome-session/sessions/gnome-classic.session
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/modes/classic.json
%{_datadir}/gnome-shell/theme/*.svg
%{_datadir}/gnome-shell/theme/gnome-classic.css
%{_datadir}/xsessions/gnome-classic.desktop

%files -n %{ext_prefix}-alternate-tab
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/alternate-tab*

%files -n %{ext_prefix}-apps-menu
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/apps-menu*

%files -n %{ext_prefix}-auto-move-windows
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
%{_datadir}/gnome-shell/extensions/auto-move-windows*

%files -n %{ext_prefix}-drive-menu
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/drive-menu*

%files -n %{ext_prefix}-launch-new-instance
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/launch-new-instance*

%files -n %{ext_prefix}-native-window-placement
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/gnome-shell/extensions/native-window-placement*

%files -n %{ext_prefix}-places-menu
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/places-menu*

%files -n %{ext_prefix}-screenshot-window-sizer
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
%{_datadir}/gnome-shell/extensions/screenshot-window-sizer*

%files -n %{ext_prefix}-systemMonitor
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/systemMonitor*

%files -n %{ext_prefix}-user-theme
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
%{_datadir}/gnome-shell/extensions/user-theme*

%files -n %{ext_prefix}-window-list
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/window-list*
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml

%files -n %{ext_prefix}-windowsNavigator
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/windowsNavigator*

%files -n %{ext_prefix}-workspace-indicator
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/workspace-indicator*
