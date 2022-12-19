import logic
import pattern
import scan


def start():
    while True:
        mode = scan.select_mode()
        if mode == '1':
            contact = scan.add_contact()
            logic.contact_add(contact)
        elif mode == '2':
            contact = scan.search_contact()
            warp = logic.take_warp()
            result = pattern.contact_search(warp, contact)
            scan.search_result(result)
