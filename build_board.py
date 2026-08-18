#!/usr/bin/env python3
"""WarriorBabe — the whole funnel, wired.

The most completely captured funnel in the swipe file: every step from opt-in to
booking confirmation. Two of those steps exist to close the gap between booking a
call and turning up to it, which is the problem we are actually trying to solve.

Run: python3 build_board.py  ->  board.html
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from boardbuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
P = os.path.expanduser("~/Downloads/Swipes/WARRIOR_BABE_Swipe/Pages")

CONFIG = {
    "OUT": os.path.join(REPO, "board.html"),
    "KICK": "Competitor swipe · captured 2 August 2026",
    "TITLE": "WarriorBabe — the whole funnel, wired",
    "BLURB": "Nikkiey Stott, the WB4 Method. Body composition for women 40+, claiming "
             "<b>17,000</b> members. Captured end to end. The interesting part is not the "
             "pitch &mdash; it is that <b>booking a call is framed as finishing an "
             "application</b>, and that a checklist sits between the booking and the call.",

    "SHOTS": {
        "optin": {
            "col": 1, "y": 120, "lane": "event", "step": "1 · Entry",
            "title": "Opt-in — name and email only",
            "url": "warriorbabe.com/macroacelerator-25-v1",
            "img": f"{P}/01_landing.png", "max_h": 1100,
            "note": "Two fields, nothing else. The redirect afterwards leaks their split "
                    "test &mdash; <b>[Macro Accelerator Split Opt]</b> &mdash; and carries "
                    "fbc, fbp, ad_id, adset_id and gclid into their CRM.",
        },
        "vsl": {
            "col": 2, "y": 120, "lane": "event", "step": "2 · Consumption",
            "title": "Training webinar — forced",
            "url": "warriorbabe.com/training-webinar-vsl1",
            "img": f"{P}/01_www_warriorbabe_com_training_webinar_vsl1.png", "max_h": 1100,
            "note": "<b>&ldquo;DO NOT Close The Window Or The Presentation Will End!&rdquo;</b> "
                    "No scrubbing, no leaving. Automation cannot get past it, which is why "
                    "the downstream pages were captured directly.",
        },
        "apply": {
            "col": 3, "y": 120, "lane": "ever", "step": "3 · Sell",
            "title": "Apply — the expired-replay page",
            "url": "warriorbabe.com/webinar-apply",
            "img": f"{P}/02_www_warriorbabe_com_webinar_apply.png", "max_h": 1100,
            "note": "A full long-form sales page for people who arrive <i>after</i> the "
                    "replay expires. The 17,000-member claim lives here. An expired replay "
                    "is a second route in, not a dead end.",
        },
        "book": {
            "col": 4, "y": 120, "lane": "back", "step": "4 · Book",
            "title": "Schedule — 45 min on Calendly",
            "url": "warriorbabe.com/schedule-booking",
            "img": f"{P}/03_www_warriorbabe_com_schedule_booking.png", "max_h": 1100,
            "note": "Headed <b>&ldquo;Final Step: Required To Complete Your "
                    "Application&rdquo;</b>. Not &ldquo;book a call&rdquo; &mdash; finishing "
                    "something already started. One line of copy, and it changes what the "
                    "click means.",
        },
        "confirm": {
            "col": 5, "y": 120, "lane": "back", "step": "5 · Confirm",
            "title": "Booked — video + pre-call checklist",
            "url": "warriorbabe.com/scheduled-success",
            "img": f"{P}/04_step1_filled.png", "max_h": 1100,
            "note": "A 3-minute video and a <b>checklist to complete before the call</b>. "
                    "Homework converts a passive booking into an active commitment.",
        },
    },

    "DATA": {
        "stack": {
            "col": 1, "y": 1500, "lane": "event", "step": "Under the hood",
            "title": "Their stack",
            "kv": [("Front end", "Webflow"), ("Forms + CRM", "HubSpot"),
                   ("Booking", "Calendly"), ("Call length", "45 min"),
                   ("Split test", "confirmed live")],
            "note": "Ordinary tools. The advantage is in the sequencing, not the software.",
        },
        "attrib": {
            "col": 2, "y": 1500, "lane": "event", "step": "What we do not have",
            "title": "Ad-level attribution at opt-in",
            "kv": [("handl_fbc", "Facebook click id"), ("handl_fbp", "browser id"),
                   ("handl_ad_id", "the exact ad"), ("handl_adset_id", "the ad set"),
                   ("handl_gclid", "Google click id"),
                   ("handl_traffic_source", "channel")],
            "note": "They can trace a booked call back to the ad set that produced it. "
                    "<b>Our paid attribution is broken and we trust only Meta's own "
                    "numbers.</b> This is the mechanism that fixes it.",
        },
        "gap": {
            "col": 4, "y": 1500, "lane": "back", "step": "The pattern",
            "title": "Work between booking and attending",
            "kv": [("WarriorBabe", "checklist + video"),
                   ("Her Closing Academy", "2:00 lock + cancel threat"),
                   ("Suprahuman", "SMS warning + reply"),
                   ("Bill Von Fumetti", "task #1 + like the post"),
                   ("UGC World", "nothing")],
            "note": "<b>Four unrelated competitors, four different markets, same "
                    "conclusion:</b> a booking is not a commitment until the lead does one "
                    "more small thing. Ours ends at the booking and we spend setter volume "
                    "chasing the gap.",
        },
        "price": {
            "col": 5, "y": 1500, "lane": "back", "step": "Not observed",
            "title": "No price anywhere",
            "kv": [("Opt-in", "no price"), ("Webinar", "cannot scrub"),
                   ("Apply page", "no price"), ("Booking", "no price"),
                   ("Where it lives", "the 45-min call")],
            "note": "Nothing is priced in any captured page. Recorded as unknown rather "
                    "than guessed.",
        },
    },

    "EDGES": [
        ("optin", "vsl"), ("vsl", "apply"), ("apply", "book"), ("book", "confirm"),
        ("optin", "attrib"), ("book", "gap"),
    ],

    "LABELS": [
        {"x": 60, "y": 60, "t": "The funnel — opt-in to booked call"},
        {"x": 60, "y": 1440, "t": "Under the hood, and the pattern across competitors"},
    ],

    "LEGEND": [("event", "Free / event"), ("ever", "Sales page"), ("back", "Call &amp; close")],
}

if __name__ == "__main__":
    build(CONFIG)
