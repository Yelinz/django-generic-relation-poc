from django.test import TestCase

from .models import Person, Team, Location


class QuestionModelTests(TestCase):
    def test_generic_relation(self):
        # create unrelated objects
        Person.objects.create(name="Sam")
        Team.objects.create(team_name="Team 2")
        Location.objects.create(location_name="Location 2")

        # create a person without a generic relation
        person1 = Person.objects.create(name="John")
        # create the target
        team = Team.objects.create(team_name="Team 1")
        # create a person with a generic relation
        person2 = Person.objects.create(name="Jane", content_object=team)
        # add the person to the generic relation
        team.persons.add(person1)

        self.assertEqual(team.persons.count(), 2)
        self.assertEqual(Person.objects.filter(team__team_name="Team 1").count(), 2)
        self.assertEqual(Team.objects.filter(persons__name="Jane").count(), 1)

        location = Location.objects.create(location_name="Location 1")
        location.persons.add(person2)

        self.assertEqual(team.persons.count(), 1)
        self.assertEqual(location.persons.count(), 1)
        self.assertEqual(person1.team.get().team_name, "Team 1")
        self.assertEqual(person1.location.count(), 0)
        self.assertEqual(person2.location.get().location_name, "Location 1")
        self.assertEqual(person2.team.count(), 0)
