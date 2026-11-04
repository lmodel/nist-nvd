package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The fields of a page of results, which every NVD API response carries.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdResponseMixin  {

  private String format;
  private ZonedDateTime timestamp;
  private int resultsPerPage;
  private int startIndex;
  private int totalResults;
  private String version;


}