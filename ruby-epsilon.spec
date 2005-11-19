Summary:	Epsilon thumbnail library for Ruby
Summary(pl):	Epsilon - biblioteka miniaturek dla jêzyka Ruby
Name:		ruby-epsilon
Version:	0.0.0
Release:	1
License:	Ruby License
Group:		Development/Languages
Source0:	http://theinternetco.net/projects/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	3acc9bcf826b29019931fbebc8f4b069
URL:		http://theinternetco.net/projects/ruby/ruby-epsilon
BuildRequires:	epsilon-devel
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby-epsilon is an extension to use the fast E17 epsilon thumbnailer.

%description -l pl
ruby-epsilon to rozszerzenie pozwalaj±ce u¿ywaæ szybkiej biblioteki
E17 do tworzenia miniaturek.

%prep
%setup -q

%build
ruby extconf.rb
%{__make}
rdoc --op rdoc *.c
rdoc --ri --op ri *.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_archdir}/*
%{ruby_ridir}/Epsilon
