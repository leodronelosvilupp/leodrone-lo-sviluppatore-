import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup

class SimpleBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Browser Semplice")
        
        # Barra degli indirizzi
        self.url_label = tk.Label(root, text="URL:")
        self.url_label.pack(pady=5)
        
        self.url_entry = tk.Entry(root, width=60)
        self.url_entry.pack(pady=5)
        
        self.go_button = tk.Button(root, text="Vai", command=self.load_page)
        self.go_button.pack(pady=5)
        
        # Area di testo per il contenuto
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
        self.text_area.pack(pady=10)
        
        # Imposta URL di default
        self.url_entry.insert(0, "https://www.google.com")
    
    def load_page(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Avviso", "Inserisci un URL valido.")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text(separator='\n', strip=True)
            
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, text)
            
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Errore", f"Errore nel caricamento della pagina: {str(e)}")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore imprevisto: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    browser = SimpleBrowser(root)
    root.mainloop()