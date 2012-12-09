# revision 21907
# category Package
# catalog-ctan /macros/latex/contrib/booktabs-de
# catalog-date 2011-03-30 22:23:52 +0200
# catalog-license gpl
# catalog-version 1.61803
Name:		texlive-booktabs-de
Version:	1.61803
Release:	2
Summary:	German version of booktabs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/booktabs-de
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.61803-2
+ Revision: 749838
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.61803-1
+ Revision: 717969
- texlive-booktabs-de
- texlive-booktabs-de
- texlive-booktabs-de
- texlive-booktabs-de

