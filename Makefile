PREFIX ?= /usr/local
SHARE_DIR = $(DESTDIR)$(PREFIX)/share/xkcd-sh
BIN_DIR = $(DESTDIR)$(PREFIX)/bin

.PHONY: install uninstall

install:
	@if [ ! -w "$(BIN_DIR)" ] && [ "$(shell id -u)" != "0" ]; then \
		echo "error: $(BIN_DIR) is not writable. run with sudo."; \
		exit 1; \
	fi
	@echo "installing xkcd.sh to $(PREFIX)..."
	mkdir -p $(SHARE_DIR) $(BIN_DIR)
	sed 's|SCRIPT_DIR=.*|SCRIPT_DIR=$(PREFIX)/share/xkcd-sh|' xkcd > /tmp/xkcd-patched
	install -Dm755 /tmp/xkcd-patched $(BIN_DIR)/xkcd
	rm /tmp/xkcd-patched
	cp -r [0-9]*/ $(SHARE_DIR)/
	@echo "done. run 'xkcd' to get started."

uninstall:
	@if [ ! -w "$(BIN_DIR)" ] && [ "$(shell id -u)" != "0" ]; then \
		echo "error: $(BIN_DIR) is not writable. run with sudo."; \
		exit 1; \
	fi
	@echo "uninstalling xkcd.sh..."
	rm -f $(BIN_DIR)/xkcd
	rm -rf $(SHARE_DIR)
	@echo "done."