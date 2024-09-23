package edu.msudenver.venue;

import org.apache.commons.lang3.exception.ExceptionUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/venues")
public class VenueController {
    @Autowired
    private VenueService venueService;

    @GetMapping(produces = "application/json")
    public ResponseEntity<List<Venue>> getVenues() {
        try {
            return ResponseEntity.ok(venueService.getVenues());
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "/{venueId}", produces = "application/json")
    public ResponseEntity<Venue> getVenue(@PathVariable Long venueId) {
        try {
            Venue venue = venueService.getVenue(venueId);
            return new ResponseEntity<>(venue, venue == null ? HttpStatus.NOT_FOUND : HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }

    @PostMapping(consumes = "application/json", produces = "application/json")
    public ResponseEntity<Venue> createCountry(@RequestBody Venue venue) {
        try {
            return new ResponseEntity<>(venueService.saveVenue(venue), HttpStatus.CREATED);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }

    @PutMapping(path = "/{venueId}",
            consumes = "application/json",
            produces = "application/json")
    public ResponseEntity<Venue> updateVenue(@PathVariable Long venueId, @RequestBody Venue updatedVenue) {
        Venue retrievedVenue = venueService.getVenue(venueId);
        if (retrievedVenue != null) {
            retrievedVenue.setName(updatedVenue.getName());
            retrievedVenue.setStreetAddress(updatedVenue.getStreetAddress());
            retrievedVenue.setType(updatedVenue.getType());
            retrievedVenue.setActive(updatedVenue.getActive());
            try {
                return ResponseEntity.ok(venueService.saveVenue(retrievedVenue));
            } catch (Exception e) {
                e.printStackTrace();
                return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
            }
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @DeleteMapping(path = "/{venueId}")
    public ResponseEntity<Void> deleteVenue(@PathVariable Long venueId) {
        try {
            return new ResponseEntity<>(venueService.deleteVenue(venueId) ?
                    HttpStatus.NO_CONTENT : HttpStatus.NOT_FOUND);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }
}
