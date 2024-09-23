package edu.msudenver.city;

import org.apache.commons.lang3.exception.ExceptionUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/cities")
public class CityController {
    @Autowired
    private CityService cityService;

    @GetMapping(produces = "application/json")
    public ResponseEntity<List<City>> getCities() {
        try {
            return ResponseEntity.ok(cityService.getCities());
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "/{countryCode}/{postalCode}", produces = "application/json")
    public ResponseEntity<City> getCity(@PathVariable String countryCode, @PathVariable String postalCode) {
        try {
            City city = cityService.getCity(countryCode, postalCode);
            return new ResponseEntity<>(city, city == null ? HttpStatus.NOT_FOUND : HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }

    @PostMapping(consumes = "application/json", produces = "application/json")
    public ResponseEntity<City> createCity(@RequestBody City city) {
        try {
            return new ResponseEntity<>(cityService.saveCity(city), HttpStatus.CREATED);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }

    @PutMapping(path = "/{countryCode}/{postalCode}",
            consumes = "application/json",
            produces = "application/json")
    public ResponseEntity<City> updateCity(@PathVariable String countryCode,
                                                 @PathVariable String postalCode,
                                                 @RequestBody City updatedCity) {
        City retrievedCity = cityService.getCity(countryCode, postalCode);
        if (retrievedCity != null) {
            retrievedCity.setName(updatedCity.getName());
            try {
                return ResponseEntity.ok(cityService.saveCity(retrievedCity));
            } catch (Exception e) {
                e.printStackTrace();
                return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
            }
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @DeleteMapping(path = "/{countryCode}/{postalCode}")
    public ResponseEntity<Void> deleteCity(@PathVariable String countryCode,
                                              @PathVariable String postalCode) {
        try {
            return new ResponseEntity<>(cityService.deleteCity(countryCode, postalCode) ?
                    HttpStatus.NO_CONTENT : HttpStatus.NOT_FOUND);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }
}
