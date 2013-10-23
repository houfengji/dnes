#.SUFFIXES: .tex .dvi .ps .pdf

#all: f.pdf

#%.pdf: %.tex
#	pdflatex $<
#	- bash -c " ( grep Rerun $*.log && pdflatex $< ) || echo noRerun "
#	- bash -c " ( grep Rerun $*.log && pdflatex $< ) || echo noRerun "

file = dnes

$(file).pdf: $(file).ps
	ps2pdf $(file).ps
$(file).ps: $(file).dvi
	dvips $(file).dvi
$(file).dvi: $(file).tex
	latex $(file).tex
	latex $(file).tex
