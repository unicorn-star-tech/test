from PyQt6.QtWidgets import QApplication
from bowling_view import BowlingView
from bowling_model import BowlingGameLogic
from bowling_controller import BowlingController


def main():
    app = QApplication([])
    model = BowlingGameLogic()
    view = BowlingView()
    # Create the controller and pass it to the view
    controller = BowlingController(model, view)
    view.controller = controller  # Add a reference to the controller in the view
    app.exec()


if __name__ == "__main__":
    main()