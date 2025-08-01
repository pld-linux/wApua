Summary:	WML browser
Summary(pl.UTF-8):	Przeglądarka WML
Name:		wApua
Version:	0.05
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://fsinfo.cs.uni-sb.de/~abe/wApua/%{name}-%{version}.tar.gz
# Source0-md5:	0133c95daee54cec758d026f0ccf0272
Patch0:		%{name}-popup.patch
URL:		http://fsinfo.cs.uni-sb.de/~abe/wApua/
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 3.0.3-26
Requires:	perl-Tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WAP WML browser.

%description -l pl.UTF-8
Przeglądarka WAP WML.

%prep
%setup -q
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/%{name}
