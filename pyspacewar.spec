#
# Conditional build:
%bcond_without	psyco		# build without python-psyco
#
%ifnarch %{ix86}
%undefine	with_psyco
%endif
Summary:	Space game with gravity
Summary(pl.UTF-8):	Kosmiczna gra z grawitacją
Name:		pyspacewar
Version:	0.9.7
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://mg.pov.lt/pyspacewar/%{name}-%{version}.tar.gz
# Source0-md5:	164128ba8a84415748ce4fbc3c2c5647
Source1:	%{name}.desktop
URL:		http://mg.pov.lt/pyspacewar/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygame-devel >= 1.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%{?with_psyco:Requires:	python-psyco}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PySpaceWar is game inspired by Spacewar, Gravity Wars, and a bit by
Star Control (I and II).

Two ships duel in a gravity field. Gravity doesn't affect the ships
themselves, but it affects missiles launched by the ships.

%description -l pl.UTF-8
PySpaceWar jest grą zainspirowaną przez Spacewar, Gravity Wars i
częściowo również przez Star Control (I i II).

Dwa statki walczą w polu grawitacyjnym. Grawitacja nie wpływa na
statki, ale wpływa na pociski wystrzelone przez nie.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{py_sitescriptdir}/%{name}/icons}

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install src/pyspacewar/icons/pyspacewar32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

# needed by splash screen
install src/pyspacewar/icons/pyspacewar48.png $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/icons

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.txt README.txt TODO.txt performance-notes.txt
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%dir %{py_sitescriptdir}/%{name}/icons
%{py_sitescriptdir}/%{name}/icons
%dir %{py_sitescriptdir}/%{name}/images
%{py_sitescriptdir}/%{name}/images
%dir %{py_sitescriptdir}/%{name}/music
%{py_sitescriptdir}/%{name}/music
%dir %{py_sitescriptdir}/%{name}/sounds
%{py_sitescriptdir}/%{name}/sounds
%{py_sitescriptdir}/*.egg-info
