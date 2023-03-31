Name:		texlive-graphicxbox
Version:	32630
Release:	2
Summary:	Insert a graphical image as a background
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/graphicxbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicxbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicxbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicxbox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines two new commands \graphicxbox and
\fgraphicxbox, which are companions to \colorbox and \fcolorbox
of the Standard LaTeX color package. The \graphicxbox command
inserts a graphical image as a background rather than a
background color, while \fgraphicxbox does the same thing, but
also draws a colored frame around the box.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/graphicxbox/graphicxbox.sty
%doc %{_texmfdistdir}/doc/latex/graphicxbox/README
%doc %{_texmfdistdir}/doc/latex/graphicxbox/doc/graphicxbox.pdf
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/IndianBlanket.eps
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/IndianBlanket.pdf
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/Wood-Brown.eps
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/Wood-Brown.pdf
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/bg_cle_tile.eps
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/grandcanyon.eps
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/grandcanyon.pdf
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/news_bgr.eps
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/news_bgr.pdf
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst.pdf
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst.tex
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst_indians.pdf
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst_indians.tex
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst_sp.pdf
%doc %{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst_sp.tex
#- source
%doc %{_texmfdistdir}/source/latex/graphicxbox/graphicxbox.dtx
%doc %{_texmfdistdir}/source/latex/graphicxbox/graphicxbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
