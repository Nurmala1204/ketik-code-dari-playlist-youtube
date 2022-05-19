from django.shortcuts import render

def Buku(request):
    judul = "Belajar Django"

    konteks = {
        'title': judul
    }
    return render(request, 'Buku.html', konteks)

def Penerbit(request):
    return HttpResponse('<h1>Halaman Penerbit</h1>')
