Summary:	Epsilon thumbnail library for Ruby
Summary(pl.UTF-8):	Epsilon - biblioteka miniaturek dla języka Ruby
Name:		ruby-epsilon
Version:	0.0.0
Release:	2
License:	Ruby License
Group:		Development/Languages
Source0:	http://theinternetco.net/projects/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	3acc9bcf826b29019931fbebc8f4b069
URL:		http://theinternetco.net/projects/ruby/ruby-epsilon
BuildRequires:	epsilon-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby-epsilon is an extension to use the fast E17 epsilon thumbnailer.

%description -l pl.UTF-8
ruby-epsilon to rozszerzenie pozwalające używać szybkiej biblioteki
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

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_archdir}/*
%{ruby_ridir}/Epsilon
