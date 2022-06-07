MODULE_NAME := llrf

OPI_VERSION := 1.8.0
OPI_DIRNAME := llrf


OPIS_HOME = /opt/epics/OPIS
OPI_DIR = /opt/epics/opi/bob
LINK_DIR = ../../OPIS

.PHONY: opiinstall	## Install the OPIs
opiinstall:
	rsync -va --delete \
	opi/ $(OPIS_HOME)/$(MODULE_NAME)/$(OPI_VERSION)/
	cd $(OPI_DIR); rm -f $(OPI_DIRNAME); ln -s $(LINK_DIR)/$(MODULE_NAME)/$(OPI_VERSION)/ $(OPI_DIRNAME)

