from django.shortcuts import render, Http404

# Data hardcoded (tanpa database)
PRODUK_LIST = [
    {
        'id': 1,
        'nama': 'Laptop ASUS ROG',
        'harga': 'Rp 15.000.000',
        'kategori': 'Elektronik',
        'deskripsi': 'Laptop gaming dengan prosesor Intel Core i7, RAM 16GB, SSD 512GB, dan GPU NVIDIA RTX 3060.',
        'stok': 5,
        'gambar': 'laptop.jpg'
    },
    {
        'id': 2,
        'nama': 'Smartphone Samsung Galaxy S23',
        'harga': 'Rp 12.000.000',
        'kategori': 'Elektronik',
        'deskripsi': 'Smartphone flagship dengan kamera 50MP, layar Dynamic AMOLED 2X, dan baterai 4500mAh.',
        'stok': 10,
        'gambar': 'hp.jpg'
    },
    {
        'id': 3,
        'nama': 'Headphone Sony WH-1000XM5',
        'harga': 'Rp 4.500.000',
        'kategori': 'Aksesoris',
        'deskripsi': 'Headphone noise-cancelling terbaik dengan kualitas suara premium dan baterai tahan 30 jam.',
        'stok': 8,
        'gambar': 'headphone.jpg'
    },
]

def homepage(request):
    return render(request, 'produk/homepage.html')

def produk_list(request):
    context = {
        'produk_list': PRODUK_LIST,
        'jumlah_produk': len(PRODUK_LIST)
    }
    return render(request, 'produk/produk_list.html', context)

def produk_detail(request, id):
    # Cari produk berdasarkan ID
    produk = None
    for p in PRODUK_LIST:
        if p['id'] == id:
            produk = p
            break
    
    if produk is None:
        raise Http404("Produk tidak ditemukan")
    
    return render(request, 'produk/produk_detail.html', {'produk': produk})

def kontak(request):
    return render(request, 'produk/kontak.html')