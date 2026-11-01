
import os


def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(person, dict) for person in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Check empty template
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        # Replace placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            invitation = invitation.replace("{" + key + "}", str(value))

        # Write output file
        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(invitation)

        except OSError as error:
            print(f"Error writing {filename}: {error}")
