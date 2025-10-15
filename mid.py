import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QFileDialog
)
from PyQt6.QtGui import QAction

class Notepad(QMainWindow):
    """간단한 메모장 어플리케이션입니다."""
    def __init__(self):
        super().__init__()
        self.current_file_path = None
        self.init_ui()

    def init_ui(self):
        """UI를 초기화합니다."""
        self.setWindowTitle("메모장")
        self.setGeometry(100, 100, 800, 600)

        # 텍스트 편집 위젯
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # 메뉴바 생성
        self.create_menu_bar()

    def create_menu_bar(self):
        """메뉴바와 액션을 생성합니다."""
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("파일")

        # 새로 만들기 액션
        new_action = QAction("새로 만들기", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        # 열기 액션
        open_action = QAction("열기", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # 저장 액션
        save_action = QAction("저장", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        # 다른 이름으로 저장 액션
        save_as_action = QAction("다른 이름으로 저장", self)
        save_as_action.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()

        # 종료 액션
        exit_action = QAction("종료", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def new_file(self):
        """새 파일을 생성합니다."""
        self.text_edit.clear()
        self.current_file_path = None
        self.setWindowTitle("메모장 - 새 파일")

    def open_file(self):
        """파일을 엽니다."""
        file_path, _ = QFileDialog.getOpenFileName(self, "파일 열기", "", "텍스트 파일 (*.txt);;모든 파일 (*.*)")
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.text_edit.setText(f.read())
                self.current_file_path = file_path
                self.setWindowTitle(f"메모장 - {file_path}")
            except Exception as e:
                print(f"파일을 여는 중 오류 발생: {e}")

    def save_file(self):
        """파일을 저장합니다."""
        if self.current_file_path:
            try:
                with open(self.current_file_path, 'w', encoding='utf-8') as f:
                    f.write(self.text_edit.toPlainText())
            except Exception as e:
                print(f"파일을 저장하는 중 오류 발생: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        """파일을 다른 이름으로 저장합니다."""
        file_path, _ = QFileDialog.getSaveFileName(self, "다른 이름으로 저장", "", "텍스트 파일 (*.txt);;모든 파일 (*.*)")
        if file_path:
            self.current_file_path = file_path
            self.save_file()
            self.setWindowTitle(f"메모장 - {file_path}")


def main():
    """어플리케이션을 실행합니다."""
    app = QApplication(sys.argv)
    notepad = Notepad()
    notepad.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()