Name:		texlive-booktabs-de
Version:	1.61803
Release:	1
Summary:	German version of booktabs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/booktabs-de
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a "translation" of the booktabs.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/booktabs-de/README-DE
%doc %{_texmfdistdir}/doc/latex/booktabs-de/booktabs-de.dtx
%doc %{_texmfdistdir}/doc/latex/booktabs-de/booktabs-de.ins
%doc %{_texmfdistdir}/doc/latex/booktabs-de/booktabs-de.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
