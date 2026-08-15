PREFIX ?= /usr/local
BINDIR ?= $(PREFIX)/bin
SCRIPT = unmask.py
TARGET = unmask

.PHONY: all install uninstall

all:
	@echo "Python script requires no compilation."
	@echo "Run 'sudo make install' to install '$(TARGET)' system-wide."

install:
	chmod +x $(SCRIPT)
	install -Dm755 $(SCRIPT) $(DESTDIR)$(BINDIR)/$(TARGET)
	@echo "Successfully installed to $(DESTDIR)$(BINDIR)/$(TARGET)"

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/$(TARGET)
	@echo "Removed $(DESTDIR)$(BINDIR)/$(TARGET)"
