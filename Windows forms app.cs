#Windows forms app (c#)

using System;
using System.Windows.Forms;

namespace SimpleWinFormsApp
{
    public class MainForm : Form
    {
        private Button button;
        private TextBox textBox;

        public MainForm()
        {
            this.Text = "Windows Forms App";
            this.Width = 300;
            this.Height = 200;

            textBox = new TextBox { Left = 50, Top = 50, Width = 200 };
            button = new Button { Text = "Click Me", Left = 100, Top = 100 };
            button.Click += (sender, e) => MessageBox.Show("Hello, " + textBox.Text);

            this.Controls.Add(textBox);
            this.Controls.Add(button);
        }
    }

    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
