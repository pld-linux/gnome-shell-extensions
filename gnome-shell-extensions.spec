%define		gshell_ver	48.0

Summary:	Modify and extend GNOME Shell functionality and behavior
Summary(pl.UTF-8):	Modyfikacje i rozszerzenia funkcjonalności i zachowania powłoki GNOME
Name:		gnome-shell-extensions
Version:	48.1
Release:	1
Group:		X11/Applications
License:	GPL v2+
Source0:	https://download.gnome.org/sources/gnome-shell-extensions/48/%{name}-%{version}.tar.xz
# Source0-md5:	ba36023178464af1fd2be4e2a7112184
URL:		https://wiki.gnome.org/Projects/GnomeShell/Extensions
BuildRequires:	meson >= 1.1.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	sassc
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ext_prefix	gnome-shell-extension

%description
GNOME Shell Extensions is a collection of extensions providing
additional and optional functionality to GNOME Shell.

Enabled extensions:
 - apps-menu
 - auto-move-windows
 - drive-menu
 - launch-new-instance
 - light-style
 - native-window-placement
 - places-menu
 - screenshot-window-sizer
 - user-theme
 - window-list
 - windowsNavigator
 - workspace-indicator

%description -l pl.UTF-8
GNOME Shell Extensions to zbiór rozszerzeń zapewniających dodatkowe i
opcjonalne funkcje powłoki GNOME.

Dostępne rozszerzenia:
 - apps-menu
 - auto-move-windows
 - drive-menu
 - launch-new-instance
 - light-style
 - native-window-placement
 - places-menu
 - screenshot-window-sizer
 - user-theme
 - window-list
 - windowsNavigator
 - workspace-indicator

%package common
Summary:	Files common to GNOME Shell Extensions
Summary(pl.UTF-8):	Pliki wspólne rozszerzeń powłoki GNOME
Group:		X11/Applications
Requires:	gnome-shell >= %{gshell_ver}
Obsoletes:	gnome-shell-extension-alternative-status-menu < 3.10.1
Obsoletes:	gnome-shell-extension-alternate-tab < 3.32.0
Obsoletes:	gnome-shell-extension-default-min-max < 3.8.3.1
Obsoletes:	gnome-shell-extension-dock < 3.8.0
Obsoletes:	gnome-shell-extension-gajim < 3.8.0
Obsoletes:	gnome-shell-extension-horizontal-workspaces < 40.0
Obsoletes:	gnome-shell-extension-static-workspaces < 3.8.3.1
Obsoletes:	gnome-shell-extension-xrandr-indicator < 3.10.1

%description common
GNOME Shell Extensions is a collection of extensions providing
additional and optional functionality to GNOME Shell. Common files and
directories needed by extensions are provided here.

%description common -l pl.UTF-8
GNOME Shell Extensions to zbiór rozszerzeń zapewniających dodatkowe i
opcjonalne funkcje powłoki GNOME. Ten pakiet zawiera wspólne pliki i
katalogi wymagane przez rozszerzenia.

%package -n gnome-classic-session
Summary:	GNOME "classic" mode session
Summary(pl.UTF-8):	Sesja trybu "klasycznego" GNOME
Group:		X11/Applications
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{ext_prefix}-apps-menu = %{version}-%{release}
Requires:	%{ext_prefix}-launch-new-instance = %{version}-%{release}
Requires:	%{ext_prefix}-light-style = %{version}-%{release}
Requires:	%{ext_prefix}-places-menu = %{version}-%{release}
Requires:	%{ext_prefix}-window-list = %{version}-%{release}
Requires:	gnome-session >= 1:3.14.0

%description -n gnome-classic-session
This package contains the required components for the GNOME Shell
"classic" mode, which aims to provide a GNOME 2-like user interface.

%description -n gnome-classic-session -l pl.UTF-8
Ten pakiet zawiera komponenty wymagane dla trybu "klasycznego" powłoki
GNOME, mającego na celu udostępnienie interfejsu użytkownika w stylu
GNOME 2.

%package -n %{ext_prefix}-apps-menu
Summary:	Application menu for GNOME Shell
Summary(pl.UTF-8):	Menu aplikacji dla powłoki GNOME
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description  -n %{ext_prefix}-apps-menu
Add a GNOME 2.x style menu for applications.

%description  -n %{ext_prefix}-apps-menu -l pl.UTF-8
To rozszerzenie dodaje menu w stylu GNOME 2.x dla aplikacji.

%package -n %{ext_prefix}-auto-move-windows
Summary:	Assign specific workspaces to applications
Summary(pl.UTF-8):	Przypisywanie konkretnych pulpitów do aplikacji
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-auto-move-windows
Lets you manage your workspaces more easily, assigning a specific
workspace to each application as soon as it creates a window, in a
manner configurable with a GSettings key.

%description -n %{ext_prefix}-auto-move-windows -l pl.UTF-8
To rozszerzenie pozwala łatwiej zarządzać pulpitami, przypisując
określony pulpit do każdej aplikacji zaraz po utworzeniu okna, w
sposób konfigurowany kluczem GSettings.

%package -n %{ext_prefix}-drive-menu
Summary:	Disk device manager in the system status area
Summary(pl.UTF-8):	Zarządca urządzeń dyskowych w obszarze stanu systemu
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-drive-menu
Adds a menu in the system status area that tracks removable disk
devices attached and offers to browse them and eject/unmount them.

%description -n %{ext_prefix}-drive-menu -l pl.UTF-8
To rozszerzenie dodaje w obszarze stanu systemu menu śledzące
podłączone odłączalne urządzenia dyskowe i pozwalające wysuwać lub
odmontowywać je.

%package -n %{ext_prefix}-launch-new-instance
Summary:	Always launch a new application instance for GNOME Shell
Summary(pl.UTF-8):	Uruchamianie zawsze nowej instancji aplikacji w powłoce GNOME
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description  -n %{ext_prefix}-launch-new-instance
This GNOME Shell extension modifies the behavior of clicking in the
dash and app launcher to always launch a new application instance.

%description  -n %{ext_prefix}-launch-new-instance -l pl.UTF-8
To rozszerzenie powłoki GNOME modyfikuje zachowanie kliknięcia w
myślnik oraz uruchamianiu aplikacji, aby zawsze uruchamiało nową
instancję aplikacji.

%package -n %{ext_prefix}-light-style
Summary:	Switch default to light style
Summary(pl.UTF-8):	Przełączenie na domyślny styl jasny
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description  -n %{ext_prefix}-light-style
Switch default to light style.

%description  -n %{ext_prefix}-light-style -l pl.UTF-8
Przełączenie na domyślny styl jasny.

%package -n %{ext_prefix}-native-window-placement
Summary:	Arrange windows in overview in a more native way
Summary(pl.UTF-8):	Układanie okien w podglądzie w bardziej natywny sposób
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-native-window-placement
This extension employs an algorithm (taken from KDE) for layouting the
thumbnails in the overview that more closely reflects the positions
and relative sizes of the actual windows, instead of using a fixed
grid.

%description -n %{ext_prefix}-native-window-placement -l pl.UTF-8
To rozszerzenie wprowadza pewnien algorytm (zaczerpnięty z KDE)
układania miniatur w podglądzie, bliżej odzwierciedlający położenia i
rozmiary względne właściwych okien, zamiast używania stałej siatki.

%package -n %{ext_prefix}-places-menu
Summary:	Places menu indicator in the system status area
Summary(pl.UTF-8):	Menu Miejsca w obszarze stanu systemu
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-places-menu
Adds a menu in the system status area that resembles the Places menu
from GNOME 2.x.

%description -n %{ext_prefix}-places-menu -l pl.UTF-8
To rozszerzenie dodaje w obszarze stanu systemu menu, przypominające
menu Miejsca z GNOME 2.x.

%package -n %{ext_prefix}-screenshot-window-sizer
Summary:	Screenshot window sizer for GNOME Shell
Summary(pl.UTF-8):	Ustalanie rozmiaru okien w powłoce GNOME przy zrzutach ekranu
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-screenshot-window-sizer
This GNOME Shell extension allows to easily resize windows for GNOME
Software screenshots.

%description -n %{ext_prefix}-screenshot-window-sizer -l pl.UTF-8
To rozszerzenie powłoki GNOME pozwala łatwo zmieniać rozmiary okien na
potrzeby zrzutów ekranu GNOME Software.

%package -n %{ext_prefix}-status-icons
Summary:	Status icons extension
Summary(pl.UTF-8):	Rozszerzenie z ikonami stanu
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-status-icons
GNOME extension to show status icons in the top bar.

%description -n %{ext_prefix}-status-icons -l pl.UTF-8
Rozszerzenie GNOME do pokazywania ikon stanu na górnej belce.

%package -n %{ext_prefix}-system-monitor
Summary:	Monitor system from the top bar
Summary(pl.UTF-8):	Monitorowanie systemu z górnej belki
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	gnome-shell-extension-systemMonitor < 3.16.0

%description -n %{ext_prefix}-system-monitor
GNOME extension to monitor system from the top bar.

%description -n %{ext_prefix}-system-monitor -l pl.UTF-8
Rozszerzenie GNOME do monitorowania systemu z górnej belki.

%package -n %{ext_prefix}-user-theme
Summary:	Let the user select a custom theme for the shell
Summary(pl.UTF-8):	Wybór własnego motywu powłoki przez użytkownika
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-user-theme
Lets the user select a custom theme for the Gnome shell. It will allow
you to apply a style from
<~/.themes/[themeName]/gnome-shell/gnome-shell.css>.

%description -n %{ext_prefix}-user-theme -l pl.UTF-8
To rozszerzenie pozwala użytkownikowi wybrać własny motyw powłoki
GNOME. Pozwala zaaplikować styl z pliku
<~/.themes/[nazwaMotywu]/gnome-shell/gnome-shell.css>.

%package -n %{ext_prefix}-window-list
Summary:	Display a window list at the bottom of the screen in GNOME Shell
Summary(pl.UTF-8):	Wyświetlanie listy okien na dole ekranu w powłoce GNOME
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-window-list
This GNOME Shell extension displays a window list at the bottom of the
screen.

%description -n %{ext_prefix}-window-list -l pl.UTF-8
To rozszerzenie powłoki GNOME wyświetla listę okien na dole ekranu.

%package -n %{ext_prefix}-windowsNavigator
Summary:	Keyboard selection of windows and work-spaces in overlay mode
Summary(pl.UTF-8):	Wybór okien i pulpitów w trybie nakładkowym z poziomu klawiatury
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-windowsNavigator
Allow keyboard selection of windows and work-spaces in overlay mode in
GNOME Shell. Switch to overview mode (press the Win or Alt+F1 key) and
press the Alt key to show numbers over windows. Press any number to
switch to the corresponding window.

%description -n %{ext_prefix}-windowsNavigator -l pl.UTF-8
To rozszerzenie pozwala na wybieranie okien i pulpitów w trybie
nakładkowym powłoki GNOME z poziomu klawiatury. Przełączenie na tryb
podglądu (naciśnięcie klawisza Win lub Alt+F1) i naciśnięcie klawisa
Alt wyświetla numery na oknach. Wpisanie liczby przełącza na
odpowiednie okno.

%package -n %{ext_prefix}-workspace-indicator
Summary:	Workspace Indicator
Summary(pl.UTF-8):	Kontrolka pulpitów
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{ext_prefix}-workspace-indicator
Put an indicator on the panel signaling in which workspace you are,
and give you the possibility of switching to another one.

%description -n %{ext_prefix}-workspace-indicator -l pl.UTF-8
To rozszerzenie umieszcza w panelu kontrolkę sygnalizującą aktualny
pulpit i pozwalający na przełączenie na inny.

%prep
%setup -q

%build
%meson \
	-Dclassic_mode=true \
	-Dextension_set=all

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n gnome-classic-session
%glib_compile_schemas

%postun -n gnome-classic-session
%glib_compile_schemas

%post -n %{ext_prefix}-apps-menu
%glib_compile_schemas

%postun -n %{ext_prefix}-apps-menu
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

%post -n %{ext_prefix}-system-monitor
%glib_compile_schemas

%postun -n %{ext_prefix}-system-monitor
%glib_compile_schemas

%post -n %{ext_prefix}-user-theme
%glib_compile_schemas

%postun -n %{ext_prefix}-user-theme
%glib_compile_schemas

%post -n %{ext_prefix}-window-list
%glib_compile_schemas

%postun -n %{ext_prefix}-window-list
%glib_compile_schemas

%post -n %{ext_prefix}-workspace-indicator
%glib_compile_schemas

%postun -n %{ext_prefix}-workspace-indicator
%glib_compile_schemas

%files common -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%dir %{_datadir}/gnome-shell/extensions

%files -n gnome-classic-session
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.extensions.classic.gschema.override
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/modes/classic.json
%{_datadir}/wayland-sessions/gnome-classic.desktop
%{_datadir}/wayland-sessions/gnome-classic-wayland.desktop
%{_datadir}/xsessions/gnome-classic.desktop
%{_datadir}/xsessions/gnome-classic-xorg.desktop

%files -n %{ext_prefix}-apps-menu
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.apps-menu.gschema.xml
%{_datadir}/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-auto-move-windows
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
%{_datadir}/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-drive-menu
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-launch-new-instance
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-light-style
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/light-style@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-native-window-placement
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-places-menu
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-screenshot-window-sizer
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
%{_datadir}/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-status-icons
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/status-icons@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-system-monitor
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.system-monitor.gschema.xml
%{_datadir}/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-user-theme
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
%{_datadir}/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-window-list
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml
%{_datadir}/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-windowsNavigator
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com

%files -n %{ext_prefix}-workspace-indicator
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.workspace-indicator.gschema.xml
%{_datadir}/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com
