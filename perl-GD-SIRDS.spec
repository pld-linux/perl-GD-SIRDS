%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	SIRDS
Summary:	GD::SIRDS Perl module - creates Single Image Random Dot Stereograms
Summary(pl):	Modu³ Perla GD::SIRDS - do tworzenia jednoobrazowych stereogramów
Name:		perl-GD-SIRDS
Version:	0.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0a7970cd1b66099e5584be972d8fb75f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::SIRDS module creates Single Image Random Dot Stereograms from a
source image or depth map. Uses GD::Image objects as its input and
output.

%description -l pl
Modu³ GD::SIRDS tworzy jednoobrazowe stereogramy z losowych kropek
na podstawie obrazu ¼ród³owego lub mapy g³êboko¶ci. U¿ywa obiektów
GD::Image jako wej¶cia i wyj¶cia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorlib}/GD/SIRDS.pm
%{_mandir}/man3/*
