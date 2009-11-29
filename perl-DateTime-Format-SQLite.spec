%define upstream_name    DateTime-Format-SQLite
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Parse and format SQLite dates and times
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Factory::Util)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Builder)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(Class::Factory::Util)
Requires: perl(DateTime::Format::Builder)

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*
