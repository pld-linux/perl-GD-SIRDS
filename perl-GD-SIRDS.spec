%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	SIRDS
Summary:	GD::SIRDS Perl module - creates Single Image Random Dot Stereograms
Summary(pl):	Modu³ Perla GD::SIRDS - do tworzenia jednoobrazowych stereogramów
Name:		perl-GD-SIRDS
Version:	0.02
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
%{__perl} Makefile.PL
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
%{perl_sitelib}/GD/SIRDS.pm
%{_mandir}/man3/*
