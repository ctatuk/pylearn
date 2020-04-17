from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html'
                        )
publications_data = [
    {
        'id': 0,
        'name': 'Моя первая публикация',
        'Date': datetime.now(),
        'text':'''
        <br><br>What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</br>

        '''},
    {
        'id': 1,
        'name': 'Моя вторая публикация',
        'Date': datetime.now(),
        'text':'''
        <br><br>Классический текст Lorem Ipsum, используемый с XVI века

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
Абзац 1.10.32 "de Finibus Bonorum et Malorum", написанный Цицероном в 45 году н.э.

"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
        '''
    },
 {
        'id': 2,
        'name': 'Моя 3я публикация',
        'Date': datetime.now(),
        'text':'''
        <br><br>Классический текст Lorem Ipsum, используемый с XVI века

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
Абзац 1.10.32 "de Finibus Bonorum et Malorum", написанный Цицероном в 45 году н.э.

"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
        '''
    }
]

def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    else:
    secret = request.POST['secret']
    name = request.POST['name']
    text = request.POST['text']

   if secret != settings SECRET_KEY:
       return render(request, 'publish.html'{
           'error': 'неправильный SECRET_KEY'
       })
    if len(name) == 0:
        return render(request, 'publish.html'
        {
            'error': 'Пустое имя'
        })
    if len(text) == 0:
        return render(request, 'publish.html'
        {
            'error': 'Пустой text'
        })
publications_data.append({
    'id': len(publications_data)
    'name': name,
    'date': datetime.now
    'text': text
})

def publications(request):
    return render(request, 'publications.html', {
        'publications': publications_data
    })

def publication(request, number):
    if number < len(publications_data):
    return render(request, 'publication.html', publications_data[number])
    else:
    return redirect('/')



def status(request):
    return HttpResponse('<h2>OK</h2>')




'''
создать view для отображения приветственной страницы и для страницы с контактами
добавить на страницы ссылки, чтобы между страницами можно было переключаться
'''