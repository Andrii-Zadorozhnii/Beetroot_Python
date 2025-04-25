from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note
from django.urls import reverse

class NoteTests(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.note = Note.objects.create(
            title='Стара назва',
            content='Старий зміст',
            author=self.user
        )

    def test_create_note(self):

        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('user_notes'),
            {
                'title': 'Нова нотатка',
                'content': 'Це зміст нової нотатки',
            }
        )

        self.assertEqual(response.status_code, 200 or 302)
        self.assertTrue(Note.objects.filter(title='Нова нотатка').exists())

    def test_edit_note(self):

        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('create_note'),
            {
                'title': 'Нова нотатка',
                'content': 'Це зміст нової нотатки',
            }
        )
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Оновлена назва')
        self.assertEqual(self.note.content, 'Оновлений зміст')
        self.assertEqual(response.status_code, 302)

    def test_edit_note_forbidden_for_unauthenticated(self):

        response = self.client.get(reverse('edit_note', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)

    def test_user_sees_only_their_notes(self):
        other_user = User.objects.create_user(username='otheruser', password='pass1234')
        Note.objects.create(title='Інша нотатка', content='Контент', author=other_user)

        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('user_notes'))
        notes = response.context['notes']
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].author, self.user)