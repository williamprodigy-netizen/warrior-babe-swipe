#!/usr/bin/env python3
"""Build the WarriorBabe swipe site.

The value here is the funnel, not the pitch: every step from opt-in to booking
confirmation was captured as a page. The webinar itself is behind a
forced-consumption player and has not been pulled, so nothing about the offer's
price is claimed below.

Run: python3 build_site.py
"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/WARRIOR_BABE_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/*.mp4"))):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     "Lead video from the opt-in step. The main training webinar sits "
                     "behind a forced-consumption player and is not captured."))
    return rows


CONFIG = {
    "SITE": "WarriorBabe — the WB4 Method",
    "CREATOR": "Nikkiey Stott",
    "ADS_KEY": "warrior_babe",
    "FUNNEL_IDS": [],
    "CAPTURED": "2 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/WARRIOR_BABE_Swipe",
    "BLURB": "Body composition for women 40+, claiming <b>17,000</b> members. The most "
             "completely captured funnel in the file — every step from opt-in to booking "
             "confirmation — and the booking step is framed as <i>finishing</i> the "
             "application rather than starting anything.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("transcripts.html", "Transcript"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Members claimed", "17,000"),
        ("ICP", "Women 40+"),
        ("Steps captured", "5"),
        ("Call length", "45 min"),
        ("Booking", "Calendly"),
        ("Stack", "HubSpot"),
        ("Price", "not observed"),
        ("Split test", "confirmed"),
    ],

    "OFFER": [
        ("Product", "WarriorBabe / WB4 Method — body composition coaching"),
        ("ICP", "Women 40+ — the page addresses &ldquo;Fabulous Forty (And Beyond)&rdquo;, "
                "45, 55, 65+"),
        ("Front end", "Free training webinar, forced-consumption player"),
        ("The call", "45-minute <b>Body Transformation Assessment</b> on Calendly"),
        ("Price", "<b>Not observed.</b> Nothing is priced anywhere in the captured pages — "
                  "the number lives on the call"),
        ("Stack", "Webflow front end, HubSpot forms and CRM, Calendly for booking"),
        ("Lead magnets", "Named mini-assets rather than one PDF — a macronutrients guide, a "
                         "menopause masterclass, an over-training workshop, a busy-mum guide"),
    ],

    "FINDINGS": [
        ("Booking is framed as finishing, not starting",
         "The scheduling page reads <b>&ldquo;Final Step: Required To Complete Your "
         "Application&rdquo;</b>. The lead is not agreeing to a sales call, they are "
         "completing something they already began. Directly copyable into our own booking "
         "step — and it costs nothing."),
        ("A pre-call checklist on the confirmation page",
         "After booking they serve a <b>3-minute video plus a checklist</b> to complete "
         "before the call. Homework converts a passive booking into an active commitment, "
         "which is the behaviour that actually precedes showing up."),
        ("They capture ad-level attribution at opt-in",
         "The opt-in posts <code>handl_fbc</code>, <code>handl_fbp</code>, "
         "<code>handl_ad_id</code>, <code>handl_adset_id</code>, <code>handl_gclid</code>, "
         "<code>handl_wbraid</code> and traffic source. They can tie a booked call back to a "
         "specific ad set. <b>We cannot — and this is the concrete fix for it.</b>"),
        ("Their split test leaked in the redirect",
         "The opt-in redirect carries <code>funnel_id=VSL-Optin-Nikkiey-WB4</code> and "
         "<code>funnel_var_id=[Macro Accelerator Split Opt]</code>. They are running a "
         "named split on the opt-in and versioning the funnel itself."),
        ("The VSL threatens to end if you leave",
         "&ldquo;DO NOT Close The Window Or The Presentation Will End!&rdquo; — forced "
         "consumption, no scrubbing, no leaving. The same posture as the timed gate on Her "
         "Closing Academy, applied earlier in the funnel."),
        ("Applications reopen after the replay expires",
         "There is a dedicated <code>/webinar-apply</code> page for people who arrive after "
         "expiry — a long-form sales page that sells the assessment directly. The expired "
         "replay is not a dead end, it is a second route in."),
    ],

    "FUNNEL": [
        ("Opt-in", "warriorbabe.com/macroacelerator-25-v1",
         "Name and email only. Redirect leaks the split-test id and full ad attribution."),
        ("Training webinar", "warriorbabe.com/training-webinar-vsl1",
         '<span class="tag bad">forced consumption</span> &ldquo;DO NOT Close The Window Or '
         'The Presentation Will End!&rdquo;'),
        ("Apply", "warriorbabe.com/webinar-apply",
         "Long-form sales page for after the replay expires. 17,000-member claim sits here."),
        ("Schedule", "warriorbabe.com/schedule-booking",
         "Calendly, 45 min. Headed <b>&ldquo;Final Step: Required To Complete Your "
         "Application&rdquo;</b>."),
        ("Confirmed", "warriorbabe.com/scheduled-success",
         "3-minute video plus a pre-call checklist before the appointment counts."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("Captured video", sorted(glob.glob(os.path.join(PKG, "Transcript/*.md")))),
    ],

    "SLIDE_PAGES": [],
    "VIDEOS": video_library(),

    "ANALYSIS": """
<div class="note"><b>Why this one matters despite being a fitness offer.</b> The product has
nothing to do with ours, but this is the most complete end-to-end funnel capture in the file,
and two of its steps are aimed squarely at the problem we actually have: getting a booked call
to turn into an attended one.</div>

<h2 class="sec">The five steps</h2>
<div class="tablewrap"><table>
<tr><th>#</th><th>Step</th><th>What it is doing</th></tr>
<tr><td>1</td><td>Opt-in</td><td>Name and email only. Lowest possible friction.</td></tr>
<tr><td>2</td><td>Webinar</td><td>Forced consumption — cannot skip, warned not to leave.</td></tr>
<tr><td>3</td><td>Apply</td><td>Long-form page, catches expired-replay traffic.</td></tr>
<tr><td>4</td><td>Schedule</td><td>Framed as <b>completing the application</b>, not booking a call.</td></tr>
<tr><td>5</td><td>Confirmed</td><td>Video + <b>pre-call checklist</b> — homework before the call.</td></tr>
</table></div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Reframe the booking step</h3><p>&ldquo;Final Step: Required To Complete
Your Application.&rdquo; A booking is a new decision; finishing something is not. One line of
copy on our scheduling page.</p></div>
<div class="card"><h3>Give them homework</h3><p>A short video and a checklist between booking
and the call. Someone who has done pre-work is far likelier to turn up than someone who simply
picked a time.</p></div>
<div class="card"><h3>Pass ad ids through the opt-in</h3><p>They carry fbc, fbp, ad_id, adset_id
and gclid into their CRM. Our paid attribution is broken and we trust only Meta's own numbers —
this is the mechanism that fixes it.</p></div>
<div class="card"><h3>Build the expired-replay page</h3><p>A dedicated sales page for people
who arrive too late, rather than a dead link. Traffic keeps arriving after an event ends.</p></div>
</div>

<h2 class="sec">Read carefully</h2>
<p><b>No price is claimed here because none was observed.</b> Nothing in the five captured
pages names a figure, and the webinar sits behind a player that cannot be scrubbed. The number
is quoted on the 45-minute assessment call.</p>
<p>The captured video is the lead-magnet piece from the opt-in step, not the main training. The
17,000-member figure is <i>their</i> claim from the apply page, not something verified.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
