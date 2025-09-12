{
  pkgs ? import <nixpkgs> {},
}:

with pkgs;

mkShell {
  buildInputs = [
    sane-backends # scanimage
    gimp
    deskew
    tesseract

    # not used by tesseract?
    # hunspellDicts.de-de
    # hunspellDicts.en-us

    # hocr editors
    # nur.repos.milahu.scribeocr
    # hocr-tools
    # nur.repos.milahu.archive-hocr-tools
    # gImageReader
    # gImageReader-qt

    # prettier

    # for 070-deskew.py
    (python3.withPackages (pp: with pp; [
      pillow
      (
        if true then opencv4 else
        # no. this takes forever to compile...
        (opencv4.override {
          enableGtk2 = true;
          gtk2 = pkgs.gtk2;
        })
      )
      numpy
      pyside6
    ]))
  ];
}
