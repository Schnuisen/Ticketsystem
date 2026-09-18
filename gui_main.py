import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QFormLayout,
    QDialogButtonBox,
    QMessageBox,
    QHeaderView,
)

from ticket_manager import (
    ticket_list,
    load_tickets,
    create_ticket,
    delete_ticket,
    update_title,
    update_description,
    update_status,
    update_priority,
    update_category,
)

from status import Status
from priority import Priority
from category import Category


# =========================================================
# CREATE / EDIT DIALOG
# =========================================================

class TicketDialog(QDialog):

    def __init__(self, parent=None, ticket=None):
        super().__init__(parent)

        self.ticket = ticket

        # -------------------------------------------------
        # Entscheiden: Create oder Edit
        # -------------------------------------------------

        if ticket is None:
            self.setWindowTitle("Create Ticket")
        else:
            self.setWindowTitle("Edit Ticket")

        self.setMinimumWidth(450)

        # -------------------------------------------------
        # Eingabefelder
        # -------------------------------------------------

        self.title_input = QLineEdit()

        self.description_input = QTextEdit()
        self.description_input.setMaximumHeight(120)

        self.status_combo = QComboBox()

        self.priority_combo = QComboBox()

        self.category_combo = QComboBox()

        # -------------------------------------------------
        # Enum-Werte in ComboBoxen eintragen
        # -------------------------------------------------

        for status in Status:
            self.status_combo.addItem(status.value)

        for priority in Priority:
            self.priority_combo.addItem(priority.value)

        for category in Category:
            self.category_combo.addItem(category.value)

        # -------------------------------------------------
        # Formular
        # -------------------------------------------------

        form_layout = QFormLayout()

        form_layout.addRow(
            "Title:",
            self.title_input
        )

        form_layout.addRow(
            "Description:",
            self.description_input
        )

        form_layout.addRow(
            "Status:",
            self.status_combo
        )

        form_layout.addRow(
            "Priority:",
            self.priority_combo
        )

        form_layout.addRow(
            "Category:",
            self.category_combo
        )

        # -------------------------------------------------
        # Buttons
        # -------------------------------------------------

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )

        self.button_box.accepted.connect(
            self.check_input
        )

        self.button_box.rejected.connect(
            self.reject
        )

        # -------------------------------------------------
        # Hauptlayout
        # -------------------------------------------------

        layout = QVBoxLayout()

        layout.addLayout(form_layout)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

        # -------------------------------------------------
        # Bei Edit vorhandene Werte anzeigen
        # -------------------------------------------------

        if ticket is not None:

            self.title_input.setText(
                ticket.title
            )

            self.description_input.setPlainText(
                ticket.description
            )

            self.status_combo.setCurrentText(
                ticket.status.value
            )

            self.priority_combo.setCurrentText(
                ticket.priority.value
            )

            self.category_combo.setCurrentText(
                ticket.category.value
            )

    # -----------------------------------------------------
    # Eingaben prüfen
    # -----------------------------------------------------

    def check_input(self):

        title = self.title_input.text().strip()

        description = (
            self.description_input
            .toPlainText()
            .strip()
        )

        if title == "":
            QMessageBox.warning(
                self,
                "Missing title",
                "Please enter a title."
            )
            return

        if description == "":
            QMessageBox.warning(
                self,
                "Missing description",
                "Please enter a description."
            )
            return

        self.accept()

    # -----------------------------------------------------
    # Werte zurückgeben
    # -----------------------------------------------------

    def get_values(self):

        title = self.title_input.text().strip()

        description = (
            self.description_input
            .toPlainText()
            .strip()
        )

        status = Status(
            self.status_combo.currentText()
        )

        priority = Priority(
            self.priority_combo.currentText()
        )

        category = Category(
            self.category_combo.currentText()
        )

        return (
            title,
            description,
            status,
            priority,
            category
        )


# =========================================================
# MAIN WINDOW
# =========================================================

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Ticket System"
        )

        self.resize(
            1000,
            600
        )

        # -------------------------------------------------
        # Central Widget
        # -------------------------------------------------

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        # -------------------------------------------------
        # Hauptlayout
        # -------------------------------------------------

        main_layout = QVBoxLayout(
            central_widget
        )

        # -------------------------------------------------
        # Überschrift
        # -------------------------------------------------

        title_label = QLabel(
            "Tickets"
        )

        title_label.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            """
        )

        main_layout.addWidget(
            title_label
        )

        # -------------------------------------------------
        # Tabelle
        # -------------------------------------------------

        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels(
            [
                "ID",
                "Title",
                "Description",
                "Status",
                "Priority",
                "Category"
            ]
        )

        # Ganze Zeile auswählen
        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        # Nur eine Zeile gleichzeitig
        self.table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        # Benutzer soll Tabelle nicht direkt bearbeiten
        self.table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        # Spalten automatisch verteilen
        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        main_layout.addWidget(
            self.table
        )

        # -------------------------------------------------
        # Buttons
        # -------------------------------------------------

        button_layout = QHBoxLayout()

        self.create_button = QPushButton(
            "Create Ticket"
        )

        self.edit_button = QPushButton(
            "Edit Ticket"
        )

        self.delete_button = QPushButton(
            "Delete Ticket"
        )

        self.refresh_button = QPushButton(
            "Refresh"
        )

        button_layout.addWidget(
            self.create_button
        )

        button_layout.addWidget(
            self.edit_button
        )

        button_layout.addWidget(
            self.delete_button
        )

        button_layout.addStretch()

        button_layout.addWidget(
            self.refresh_button
        )

        main_layout.addLayout(
            button_layout
        )

        # -------------------------------------------------
        # Buttons mit Funktionen verbinden
        # -------------------------------------------------

        self.create_button.clicked.connect(
            self.open_create_dialog
        )

        self.edit_button.clicked.connect(
            self.open_edit_dialog
        )

        self.delete_button.clicked.connect(
            self.delete_selected_ticket
        )

        self.refresh_button.clicked.connect(
            self.refresh_table
        )

        # Doppelklick auf Ticket = Edit
        self.table.doubleClicked.connect(
            self.open_edit_dialog
        )

        # -------------------------------------------------
        # Tabelle beim Start anzeigen
        # -------------------------------------------------

        self.refresh_table()

    # =====================================================
    # Tabelle aktualisieren
    # =====================================================

    def refresh_table(self):

        self.table.setRowCount(0)

        for ticket in ticket_list:

            row = self.table.rowCount()

            self.table.insertRow(
                row
            )

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    str(ticket.ticket_id)
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    ticket.title
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    ticket.description
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    ticket.status.value
                )
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    ticket.priority.value
                )
            )

            self.table.setItem(
                row,
                5,
                QTableWidgetItem(
                    ticket.category.value
                )
            )

    # =====================================================
    # Ausgewählte Ticket-ID
    # =====================================================

    def get_selected_ticket(self):

        row = self.table.currentRow()

        if row == -1:
            return None

        id_item = self.table.item(
            row,
            0
        )

        if id_item is None:
            return None

        ticket_id = int(
            id_item.text()
        )

        for ticket in ticket_list:

            if ticket.ticket_id == ticket_id:
                return ticket

        return None

    # =====================================================
    # CREATE
    # =====================================================

    def open_create_dialog(self):

        dialog = TicketDialog(
            self
        )

        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:

            (
                title,
                description,
                status,
                priority,
                category
            ) = dialog.get_values()

            create_ticket(
                title,
                description,
                status,
                priority,
                category
            )

            self.refresh_table()

    # =====================================================
    # EDIT
    # =====================================================

    def open_edit_dialog(self):

        ticket = self.get_selected_ticket()

        if ticket is None:

            QMessageBox.information(
                self,
                "No ticket selected",
                "Please select a ticket first."
            )

            return

        dialog = TicketDialog(
            self,
            ticket
        )

        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:

            (
                title,
                description,
                status,
                priority,
                category
            ) = dialog.get_values()

            update_title(
                ticket.ticket_id,
                title
            )

            update_description(
                ticket.ticket_id,
                description
            )

            update_status(
                ticket.ticket_id,
                status
            )

            update_priority(
                ticket.ticket_id,
                priority
            )

            update_category(
                ticket.ticket_id,
                category
            )

            self.refresh_table()

    # =====================================================
    # DELETE
    # =====================================================

    def delete_selected_ticket(self):

        ticket = self.get_selected_ticket()

        if ticket is None:

            QMessageBox.information(
                self,
                "No ticket selected",
                "Please select a ticket first."
            )

            return

        answer = QMessageBox.question(
            self,
            "Delete Ticket",
            (
                f"Do you really want to delete "
                f"ticket #{ticket.ticket_id}?\n\n"
                f"{ticket.title}"
            ),
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )

        if answer == QMessageBox.StandardButton.Yes:

            delete_ticket(
                ticket.ticket_id
            )

            self.refresh_table()


# =========================================================
# PROGRAM START
# =========================================================

app = QApplication(
    sys.argv
)

# Tickets aus JSON laden
load_tickets()

# Hauptfenster erstellen
window = MainWindow()

# Fenster anzeigen
window.show()

# Event Loop starten
sys.exit(
    app.exec()
)