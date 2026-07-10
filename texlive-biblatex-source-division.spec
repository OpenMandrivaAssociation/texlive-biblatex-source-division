%global tl_name biblatex-source-division
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4.2
Release:	%{tl_revision}.1
Summary:	References by division in classical sources
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-source-division
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-source-division.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-source-division.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to make reference to "division marks" (such
as book, chapter, section), in the document being referenced, in
addition to the page-based references that BibTeX-based citations have
always had. The citation is made in the same way as the LaTeX standard,
but what's inside the square brackets may include the "division"
specification, as in \cite[(<division spec.>)<page number>]{<document>}

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-source-division
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-source-division
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-source-division/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-source-division/biblatex-source-division.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-source-division/biblatex-source-division.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-source-division/biblatex-source-division.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-source-division/latexmkrc
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-source-division/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-source-division/biblatex-source-division.sty
