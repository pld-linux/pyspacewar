#
# Conditional build:
%bcond_without	psyco		# build without python-psyco
#
Summary:	Space game with gravity
Summary(pl):	Kosmiczna gra z grawitacj�
Name:		pyspacewar
Version:	0.9.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://mg.pov.lt/pyspacewar/%{name}-%{version}.tar.gz
# Source0-md5:	e7e738bc28cb9609041cb65f731e67b2
Source1:	%{name}.desktop
URL:		http://mg.pov.lt/pyspacewar/
BuildRequires:	python-devel >= 2.3
%{?with_psyco:BuildRequires:	python-psyco}
BuildRequires:	python-pygame-devel >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PySpaceWar is game inspired by Spacewar, Gravity Wars, and a bit by
Star Control (I and II).

Two ships duel in a gravity field. Gravity doesn't affect the ships
themselves, but it affects missiles launched by the ships.

%description -l pl
PySpaceWar jest gr� zainspirowan� przez Spacewar, Gravity Wars i
cz�ciowo r�wnie� przez Star Control (I i II).

Dwa statki walcz� w polu grawitacyjnym. Grawitacja nie wp�ywa na
statki, ale wp�ywa na pociski wystrzelone przez nie.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.txt README.txt TODO.txt performance-notes.txt
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{py_sitescriptdir}/*