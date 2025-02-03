Summary:	BigNum multi-precision integer math library
Summary(pl.UTF-8):	BigNum - biblioteka arytmetyki całkowitej wielokrotnej precyzji
Name:		bnlib
Version:	1.1.4
Release:	2
License:	GPL v2 or commercial
Group:		Libraries
Source0:	http://philzimmermann.com/bnlib/bnlib114.zip
# Source0-md5:	1b4ff1e1f41c812db03a7c44b27d44ee
Patch0:		%{name}-ac.patch
Patch1:		%{name}-shared.patch
URL:		http://philzimmermann.com/EN/bnlib/bnlib.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a multi-precision math library designed to be very portable,
reasonably clean and easy to use, have very liberal bounds on the
sizes of numbers that can be represented, but above all to perform
extremely fast modular exponentiation. It has some limitations, such
as representing positive numbers only, and supporting only odd moduli,
which simplify it without impairing this ability.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę matematyczną wielokrotnej precyzji,
zaprojektowaną jako bardzo przenośna, w miarę przejrzysta i łatwa w
użyciu, mająca liberalne ograniczenia na dopuszczalne rozmiary liczb,
a przede wszystkim bardzo szybko wykonująca potęgowanie modulo. Ma
pewne ograniczenia, takie jak reprezentowanie wyłącznie liczb
dodatnich czy obsługa wyłącznie nieparzystych współczynników.

%package devel
Summary:	Header files for BigNum library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki BigNum
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for BigNum library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki BigNum.

%package static
Summary:	Static BigNum library
Summary(pl.UTF-8):	Statyczna biblioteka BigNum
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static BigNum library.

%description static -l pl.UTF-8
Statyczna biblioteka BigNum.

%prep
%setup -q -c
# sanitize first
%{__rm} -r __MACOSX
%{__mv} bnlib114/* .
%{__rm} -r bnlib114
%patch -P 0 -p1
%patch -P 1 -p1

# extract licensing information
head -n29 legal.c > LEGAL

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LEGAL README.bn bn.doc
%attr(755,root,root) %{_libdir}/libbn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbn.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbn.so
%{_libdir}/libbn.la
%{_includedir}/bn.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libbn.a
