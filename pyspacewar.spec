#
# Conditional build:
%bcond_without	psyco		# build without python-psyco
#
%ifnarch %{ix86}
%undefine	with_psyco
%endif
Summary:	Space game with gravity
Summary(pl.UTF-8):   Kosmiczna gra z grawitacją
Name:		pyspacewar
Version:	0.9.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://mg.pov.lt/pyspacewar/%{name}-%{version}.tar.gz
# Source0-md5:	d9515eb2584efd9fa43f6fa49b9761b2
Source1:	%{name}.desktop
URL:		http://mg.pov.lt/pyspacewar/
BuildRequires:	python-devel >= 1:2.4
%{?with_psyco:BuildRequires:	python-psyco}
BuildRequires:	python-pygame-devel >= 1.6
BuildRequires:	rpm-pythonprov
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \
	--install-data=%{_datadir} \
	--install-lib=%{py_sitescriptdir} \
	--install-scripts=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install src/pyspacewar/images/%{name}-32x32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.txt README.txt TODO.txt performance-notes.txt
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{py_sitescriptdir}/*
