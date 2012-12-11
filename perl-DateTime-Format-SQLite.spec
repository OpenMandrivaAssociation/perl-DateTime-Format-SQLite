%define upstream_name    DateTime-Format-SQLite
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Parse and format SQLite dates and times
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Factory::Util)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Builder)

BuildArch:	noarch

Requires:	perl(Class::Factory::Util)
Requires:	perl(DateTime::Format::Builder)

%description
This module understands the formats used by SQLite for its 'date',
'datetime' and 'time' functions. It can be used to parse these formats in
order to create the DateTime manpage objects, and it can take a DateTime
object and produce a timestring accepted by SQLite.

*NOTE:* SQLite does not have real date/time types but stores everything as
strings. This module deals with the date/time strings as
understood/returned by SQLite's 'date', 'time', 'datetime', 'julianday' and
'strftime' SQL functions. You will usually want to store your dates in one
of these formats.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 654913
- rebuild for updated spec-helper

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 477620
- update to 0.11

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-3mdv2010.1
+ Revision: 471496
- adding missing requires:

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-2mdv2010.1
+ Revision: 471456
- bump mkrel
- adding missing requires:

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.1
+ Revision: 471295
- adding missing buildrequires:
- import perl-DateTime-Format-SQLite


* Sun Nov 29 2009 cpan2dist 0.10-1mdv
- initial mdv release, generated with cpan2dist
