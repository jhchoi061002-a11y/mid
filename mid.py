import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

def main():
    """PyQt6를 사용하여 기본창을 띄우는 함수입니다."""
    app = QApplication(sys.argv)
    
    window = QWidget()
    window.setWindowTitle("메모장")
    window.setGeometry(100, 100, 300, 200)
    
    label = QLabel("메모장을 만들어봐요", parent=window)
    label.move(110, 80)
    
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
