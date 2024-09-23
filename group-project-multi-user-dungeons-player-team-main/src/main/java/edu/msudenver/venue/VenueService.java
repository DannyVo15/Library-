package edu.msudenver.venue;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;
import java.util.List;
import java.util.NoSuchElementException;

@Service
public class VenueService {
    @Autowired
    private VenueRepository venueRepository;

    @PersistenceContext
    private EntityManager entityManager;

    public List<Venue> getVenues() {
        return venueRepository.findAll();
    }

    public Venue getVenue(Long venueId) {
        try {
            return venueRepository.findById(venueId).get();
        } catch(NoSuchElementException | IllegalArgumentException e) {
            e.printStackTrace();
            return null;
        }
    }

    @Transactional
    public Venue saveVenue(Venue venue) {
        venue = venueRepository.saveAndFlush(venue);
        entityManager.refresh(venue);
        return venue;
    }
    public boolean deleteVenue(Long venueId) {
        try {
            if(venueRepository.existsById(venueId)) {
                venueRepository.deleteById(venueId);
                return true;
            }
        } catch(IllegalArgumentException e) {
            e.printStackTrace();
        }

        return false;
    }
}
