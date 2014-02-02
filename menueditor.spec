Summary:	Menu Editor - an editor for IceWM's menus and console
Summary(pl.UTF-8):	Menu Editor - edytor menu i konsoli IceWM
Name:		menueditor
Version:	1.3.4
Release:	1
License:	GPL-like
Group:		X11/Applications
Source0:	http://wolfsinger.com/~wolfpack/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	f792f5bef072bd0e1d9bc0304434124d
Patch0:		%{name}-verbose.patch
URL:		http://freecode.com/projects/menueditor
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Menu Editor is an editor for IceWM's menus and console.

%description -l pl.UTF-8
Menu Editor to edytor menu i konsoli IceWM.

%prep
%setup -q
%patch0 -p1

%build
./configure Linux -v \
	--prefix=%{_prefix}

%{__make} \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} %{!?debug:-fomit-frame-pointer} -ffast-math -D__USE_BSD -DPREFIX=\\\"/usr\\\" `imlib-config --cflags` -DHAVE_IMLIB `gtk-config --cflags`" \
	LIB_DIRS=

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INSTBINFLAGS="-m755"

bunzip2 $RPM_BUILD_ROOT%{_mandir}/man1/*.1.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_bindir}/menueditor
%{_datadir}/menueditor
%{_mandir}/man1/menueditor.1*
%{_pixmapsdir}/menueditor.xpm
